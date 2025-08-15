import pyautogui
import json
import time
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

config_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'data', 'default.json')
)
try:
    with open(config_path) as f:
        data = json.load(f)
except FileNotFoundError:
    print(Fore.RED + f"Config file not found at {config_path}")
    sys.exit(1)


mouse = pyautogui.position()
initial_mouse_x = mouse.x
mouse_change_flag = False

print(sys.argv)


def kill_terminal_mouse_move():
    """Set the flag if the user has moved the mouse manually."""
    global mouse_change_flag
    if pyautogui.position().x != initial_mouse_x:
        mouse_change_flag = True


def copy_right():
    """Final message after the loop finishes or is interrupted."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "* -Thanks for coming online — it's been very hard to keep your PC awake- *")
    print(Fore.CYAN + Style.BRIGHT + data.get('copyright', ''))
    print(Fore.GREEN + Style.BRIGHT + f"love this project <3 follow -{data.get('follow', '')}")


def change_mouse(timedelay=None, timeinms=None):
    """Oscillate the mouse up/down until manual movement or iteration limit."""
    global mouse, mouse_change_flag

    # Fallback to JSON values
    timedelay = timedelay or data.get('timedelay', 100)
    timeinms = timeinms or data.get('TimeinMS', 500)
    multiple_check = data.get('MultipleCheck', 2)
    mouse_move = data.get('MouseMove', 100)

    print(Fore.MAGENTA + f" -  Current mouse position {{'x': {mouse.x}, 'y': {mouse.y}}} -")

    for i in range(timeinms):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + '-' * 53)

        if mouse_change_flag:
            break
        
        if i % multiple_check == 0:
            new_y = mouse.y + mouse_move
            print(Fore.YELLOW + f"      - moving to x:{mouse.x}, y:{new_y} -")
        else:
            new_y = mouse.y - mouse_move
            print(Fore.YELLOW + f"      - moving to x:{mouse.x}, y:{new_y} -")

        
        pyautogui.moveTo(mouse.x, new_y, duration=timedelay / 1000)
        mouse = pyautogui.position()

        
        kill_terminal_mouse_move()
        print(Fore.CYAN + '-' * 53)

    copy_right()


if __name__ == '__main__':
    try:
        change_mouse(data.get('timedelay'), data.get('TimeinMS'))
    except KeyboardInterrupt:
        print("Script interrupted manually.")

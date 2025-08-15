import pyautogui
import time
import os
import sys
import json
from colorama import init, Fore, Style

init(autoreset=True)

# Default constants
DEFAULTS = {
    "MouseMove": 2,
    "backup_MouseMove": 100,
    "timedelay": 100,
    "TimeinMS": 5000000,
    "MultipleCheck": 2,
    "copyright": "Copyright @ 2025 Hariom Gola. All Right Reserved Not to be Used for Making profit",
    "follow": "github.com/hariomgola"
}

config_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'data', 'default.json')
)
if os.path.exists(config_path):
    try:
        with open(config_path) as f:
            data = json.load(f)
    except Exception as e:
        print(Fore.RED + f"Error reading config file: {e}")
        data = DEFAULTS
else:
    print(Fore.YELLOW + f"Config file not found at {config_path}, using defaults.")
    data = DEFAULTS

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
    """Final message after the loop finishes or is interrupted, with countdown."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "* -Thanks for coming online — it's been very hard to keep your PC awake- *")
    print(Fore.CYAN + Style.BRIGHT + data['copyright'])
    print(Fore.GREEN + Style.BRIGHT + f"love this project <3 follow -{data['follow']}")
    print(Fore.RED + "\nThis window will close in 10 seconds...")

    for i in range(10, 0, -1):
        print(Fore.YELLOW + f"Closing in {i} seconds...", end='\r')
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')


def change_mouse(timedelay=None, timeinms=None):
    """Oscillate the mouse up/down until manual movement or iteration limit."""
    global mouse, mouse_change_flag

    timedelay = timedelay or data['timedelay']
    timeinms = timeinms or data['TimeinMS']
    multiple_check = data['MultipleCheck']
    mouse_move = data['MouseMove']

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
        change_mouse(data['timedelay'], data['TimeinMS'])
    except KeyboardInterrupt:
        print("Script interrupted manually.")

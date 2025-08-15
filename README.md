# PC Awake Assistant

A lightweight Python script that gently nudges your mouse to keep your PC awake when you’re away. It oscillates your cursor up and down at configurable intervals, detects manual movement to stop gracefully, and displays a friendly 10-second countdown before closing.

---

## Features

- Keeps your system awake by simulating natural mouse movement
- Configurable delays, movement distance, and iteration limits
- Detects manual mouse movement to exit early
- Loads settings from a JSON config or falls back to sensible defaults
- Colorful, easy-to-read console output
- Final “thank you” message with a 10-second countdown before the console window closes

---

## Requirements

- Python 3.6 or higher
- `pyautogui`
- `colorama`

---

## Installation

1. Clone the repository to your local machine
2. Navigate into the project folder
3. Install dependencies with pip

   ```bash
   git clone https://github.com/hariomgola/pc-awaker.git
   cd pc-awaker
   pip install pyautogui colorama
   ```

---

```bash
python awaken.py <timedelay_in_ms> <iteration_count>
# Example:
python awaken.py 200 1000000
```

## Project Status

    - Completed

## Made with :heart:

Portfolio :computer: https://hariomgola.github.io/

### :point_right: `I see it I love it I code it`

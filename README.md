# Simple Rage Quit Roblox Python Program

A small Python script that automatically closes Roblox when your health bar turns red. Perfect for those “oh no” moments when you want to avoid dying in-game.

## Features

- Monitors a single pixel representing your health bar.
- Automatically exits Roblox if it detects low health (red).
- Lightweight and requires only `pyautogui` and `time`.
- Supports fullscreen and windowed mode (just adjust the pixel coordinates).  

## Requirements

- Python 3.x  
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/)

Install `pyautogui` with:

```bash
pip install pyautogui
```

## Usage

1. Make sure Roblox is running in **fullscreen** or **windowed mode**.  
2. Adjust the pixel coordinates in the script if using windowed mode:

```python
pixelset = X, Y = 1785, 35  # fullscreen
# x1785 y55 for windowed
```

3. Run the script:

```bash
python ragequit_roblox.py
```

4. The script will watch the specified pixel. When it detects red (low health), it will automatically close Roblox.

## Notes

- Ensure Roblox is in the foreground, and avoid moving your mouse to the top-left corner—`pyautogui` has a fail-safe there.  
- Adjust `tolerance` in the `colorisclose` function if your health bar uses slightly different shades of red.

## Disclaimer

This script is for personal use and automation convenience. Use responsibly and at y
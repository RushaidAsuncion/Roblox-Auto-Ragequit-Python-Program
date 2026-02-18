#simpleragequitrobloxpythonprogrambyrushaid
#all you need is pyautogui and time
#makesure your on fullsceen you have to change the xy for windowed
import pyautogui
import time

pyautogui.FAILSAFE = True

pixelset = X, Y = 1785, 35 # x1785 y55 for windowed and x1785 y35 for fullscreen

print(f"Watching pixel at {pixelset}")

def colorisclose(pixel, target, tolerance=20):
    red, green, blue = pixel
    tred, tgreen, tblue = target
    return abs(red - tred) <= tolerance and abs(green - tgreen) <= tolerance and abs(blue - tblue) <= tolerance


targetredpixels = (255, 26, 0)

while True:
    pixelcolor = pyautogui.pixel(X, Y)

    
    conditionred = colorisclose(pixelcolor, targetredpixels, tolerance=20)
    
    
    if conditionred:
        print("closing roblox")
        pyautogui.hotkey("alt", "f4")
        time.sleep(0.4) 
        pyautogui.hotkey("alt", "f4")
        break 
    
    time.sleep(0.1) 


import sys, time

def install(package):
    try:
        __import__(package)
    except:
        import subprocess
        subprocess.call([sys.executable, "-m", "pip", "install", package])

print("LOADING PACKAGES (will take longer the first time)...\n")
time.sleep(0.15)

install("pyautogui")
install("keyboard")
import pyautogui, keyboard
pyautogui.FAILSAFE = False

print("\nloaded!\n")
time.sleep(0.15)

key = input("Key the mouse should go down and up on (one character): ")

while True:
    if keyboard.is_pressed(key):
      pyautogui.mouseDown()
    else:
      pyautogui.mouseUp()
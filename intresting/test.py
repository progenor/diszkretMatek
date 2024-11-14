from win32gui import *
from win32api import *
from win32con import *

def flash_screen():
    hdc = GetDC(0) # Get the screen as a Device Context object
    x, y = GetSystemMetrics(0), GetSystemMetrics(1) # retrieve monitor size
    PatBlt(hdc, 0, 0, x, y, PATINVERT) # invert the device context
    Sleep(10) # Sleep for 10 milliseconds
    PatBlt(hdc, 0, 0, x, y, PATINVERT) # invert back to normal
    DeleteDC(hdc) # clean up memory

if __name__ == "__main__":
    yes = 10
    while yes:
        yes -= 1
        flash_screen()
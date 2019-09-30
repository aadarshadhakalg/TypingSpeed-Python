import sys
from cx_Freeze import setup, Executable


base = None

if (sys.platform == "win32"):
    base = "Win32GUI"

if sys.platform == 'win64':
    base = "Win64GUI"

setup(
    name = "Typing Speed",
    version = "1.0",
    description = "A typing speed calculator tool. | Developed by Aadarsha Dhakal",
    executables = [Executable("tspeed_gui.py", base = base, shortcutName="Typing Speed",shortcutDir="DesktopFolder",icon='Tspeed.ico')])

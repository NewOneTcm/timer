import sys
import platform

def lock_screen():
    if platform.system() == 'Windows':
        # Code to lock screen on Windows
        import ctypes
        ctypes.windll.user32.LockWorkStation()
    elif platform.system() == 'Linux':
        # Code to lock screen on Linux
        import subprocess
        subprocess.run(['gnome-screensaver-command', '--lock'])
    elif platform.system() == 'Darwin':
        # Code to lock screen on macOS
        subprocess.run('pmset displaysleepnow', shell=True)
    else:
        print("Locking screen is not supported on this platform.")

if __name__ == "__main__":
    lock_screen()

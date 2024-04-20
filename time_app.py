import sys
from PyQt5.QtWidgets import QApplication
from ui_timer import TimerUI  # Assuming TimerUI is the class that defines the UI

def main():
    app = QApplication(sys.argv)
    window = TimerUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

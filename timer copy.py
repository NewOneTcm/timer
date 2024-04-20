import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_timer_design import Ui_MainWindow
from PyQt5.QtCore import QTimer



class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.time_remaining = 25 * 60 * 1000  # Initial time: 25 minutes
        self.timer.timeout.connect(self.update_timer)
        self.ui.pushButton_start.clicked.connect(self.start_timer)
        self.ui.pushButton_stop.clicked.connect(self.stop_timer)
        self.ui.pushButton_set.clicked.connect(self.set_timer)
        self.update_timer_display()

    def start_timer(self):
        self.timer.start(1000)  # Timer updates every second

    def stop_timer(self):
        self.timer.stop()

    def set_timer(self):
        # Add functionality to set the timer duration
        pass

    def update_timer(self):
        self.time_remaining -= 1000
        self.update_timer_display()
        if self.time_remaining <= 0:
            self.timer.stop()
            # Add functionality for when the timer reaches 0

    def update_timer_display(self):
        minutes = self.time_remaining // 60000
        seconds = (self.time_remaining % 60000) // 1000
        self.ui.label.setText(f"{minutes:02}:{seconds:02}")


def main():
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_timer_design import Ui_MainWindow

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("生姜大叔的番茄钟")
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Timer updates every second
        self.time_remaining = 25 * 60 * 1000  # Initial time: 25 minutes
        self.timer.timeout.connect(self.update_timer)
        self.ui.pushButton_start.clicked.connect(self.start_timer)
        self.ui.pushButton_stop.clicked.connect(self.stop_timer)
        self.ui.pushButton_set.clicked.connect(self.set_timer)
        self.ui.pushButton_stop.setEnabled(False)  # Initially disable stop button
        self.ui.pushButton_stop.clicked.connect(self.stop_and_reset_timer)  # Connect stop button to reset function
        self.break_timer = QTimer(self)
        self.break_timer.setInterval(5 * 60 * 1000)  # 5 minutes break
        self.break_timer.timeout.connect(self.start_break)

    def start_timer(self):
        self.timer.start()
        self.ui.pushButton_start.setEnabled(False)  # Disable start button
        self.ui.pushButton_stop.setEnabled(True)   # Enable stop button

    def stop_timer(self):
        self.timer.stop()
        self.ui.pushButton_start.setEnabled(True)  # Enable start button
        self.ui.pushButton_stop.setEnabled(False)  # Disable stop button

    def stop_and_reset_timer(self):
        self.stop_timer()
        self.time_remaining = 25 * 60 * 1000  # Reset timer
        self.update_timer_display()
        self.break_timer.start()  # Start break timer

    def set_timer(self):
        # Add functionality to set the timer duration
        pass

    def update_timer(self):
        self.time_remaining -= 1000
        if self.time_remaining <= 0:
            self.timer.stop()
            self.stop_and_reset_timer()
        self.update_timer_display()

    def start_break(self):
        # Add functionality for starting break
        pass

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

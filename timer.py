from PyQt5.QtCore import QTimer, QObject, pyqtSignal

class TimerWorker(QObject):
    time_remaining_signal = pyqtSignal(int, int)
    timer_finished_signal = pyqtSignal()  # Signal to indicate timer finished

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = 1 * 10  # 25 minutes initial time

    def start_timer(self):
        self.timer.start(1000)  # Start timer with 1-second interval

    def stop_timer(self):
        self.timer.stop()  # Stop the timer

    def update_timer(self):
        self.time_remaining -= 1
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.time_remaining_signal.emit(minutes, seconds)  # Emit signal with updated time

        if self.time_remaining == 0:  # Check if time has reached 00:00
            self.stop_timer()  # Stop the timer
            self.timer_finished_signal.emit()  # Emit signal to indicate timer finished

from PyQt5.QtWidgets import QMainWindow
from ui_timer_design import Ui_MainWindow
from timer import TimerWorker
from audio_handler import AudioHandler

class TimerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = TimerWorker()
        self.worker.time_remaining_signal.connect(self.update_display)
        self.ui.pushButton_start.clicked.connect(self.start_timer)
        self.ui.pushButton_stop.clicked.connect(self.stop_timer)

        # Set window title
        self.setWindowTitle("生姜大叔的番茄钟")

        # Default time display
        self.default_time_display = "25:00"

        # Initialize audio handler
        self.audio_handler = AudioHandler('bell.wav')    
        
        self.worker.timer_finished_signal.connect(self.play_sound)  # Connect timer finished signal
        

    def start_timer(self):
        self.worker.start_timer()

    def stop_timer(self):
        self.worker.stop_timer()
        self.ui.label.setText(self.default_time_display)  # Revert to default time display

    def update_display(self, minutes, seconds):
        self.ui.label.setText(f"{minutes:02}:{seconds:02}")

        # Check if time has reached 00:00
        if minutes == 0 and seconds == 0:
            self.worker.stop_timer()  # Stop the timer
            self.ui.label.setText(self.default_time_display)  # Revert to default time display
            self.audio_handler.play_sound()  # Play sound when timer finishes

    def play_sound(self):
        self.audio_handler.play_sound()

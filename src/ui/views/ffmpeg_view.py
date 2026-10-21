from core.ffmpeg_checker import ensure_ffmpeg
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class FFmpegWorker(QThread):
    
    status_changed = pyqtSignal(str)
    finished_signal = pyqtSignal(bool)

    def run(self):
        success = ensure_ffmpeg(status_callback=self.status_changed.emit)
        self.finished_signal.emit(success)


class FFmpegView(QWidget):
    
    check_finished = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(60, 10, 60, 30)
        layout.addStretch(1)

        text_block = QWidget()
        text_layout = QVBoxLayout(text_block)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(12)

        title = QLabel("Environment Verification")
        title.setObjectName("SectionTitle")

        self.status_label = QLabel("Comprobando entorno del sistema...")
        self.status_label.setObjectName("BodyText")

        self.sub_status_label = QLabel("")
        self.sub_status_label.setObjectName("SubStatusText")

        text_layout.addWidget(title)
        text_layout.addWidget(self.status_label)
        text_layout.addWidget(self.sub_status_label)

        layout.addWidget(text_block, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)

    def start_verification(self):
        self.worker = FFmpegWorker()
        self.worker.status_changed.connect(self._update_status)
        self.worker.finished_signal.connect(self._on_finished)
        self.worker.start()

    def _update_status(self, message: str):
        if "SUCCESS:" in message:
            self.status_label.setText(message)
            self.status_label.setStyleSheet("color: #50fa7b;")
            self.sub_status_label.setText("")
        elif "ERROR:" in message:
            self.status_label.setText(message)
            self.status_label.setStyleSheet("color: #ffb86c;")
        elif "FAILED:" in message:
            self.status_label.setText(message)
            self.status_label.setStyleSheet("color: #ff5555;") 
        else:
            self.sub_status_label.setText(message)

    def _on_finished(self, success: bool):
        self.check_finished.emit(success)
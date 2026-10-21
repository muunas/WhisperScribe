from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class WelcomeView(QWidget):
    start_requested = pyqtSignal()

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
        text_layout.setSpacing(8)

        welcome_title = QLabel("Welcome")
        welcome_title.setObjectName("SectionTitle")

        welcome_text = QLabel(
            "WhisperScribe is a desktop application designed to transcribe\n"
            "your audio files into text quickly, locally, and with total privacy.\n"
            "Powered by advanced AI models, it converts recordings,\n"
            "interviews, and voice notes into text in seconds—without relying\n"
            "on cloud services or touching the terminal."
        )
        welcome_text.setObjectName("BodyText")

        text_layout.addWidget(welcome_title)
        text_layout.addWidget(welcome_text)

        layout.addWidget(text_block, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(35)

        start_button = QPushButton("Start")
        start_button.setObjectName("ActionButton")
        start_button.setFixedWidth(260)
        start_button.setCursor(Qt.CursorShape.PointingHandCursor)
        start_button.clicked.connect(self.start_requested.emit)

        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QProgressBar, QPushButton


class ProgressView(QWidget):
    
    download_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 20, 50, 25)
        main_layout.setSpacing(15)

        main_layout.addStretch(1)

        card = QFrame()
        card.setObjectName("ProgressCard")
        card.setFixedSize(540, 280)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(30, 25, 30, 25)
        card_layout.setSpacing(12)

        title = QLabel("Transcription process")
        title.setObjectName("ProgressTitle")

        self.status_label = QLabel("Initializing model on CPU...")
        self.status_label.setObjectName("ProgressStatusLabel")
        self.status_label.setWordWrap(True)

        self.percentage_label = QLabel("Percentage: 0%")
        self.percentage_label.setObjectName("PercentageLabel")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)

        self.download_btn = QPushButton("Download transcription.txt")
        self.download_btn.setObjectName("DownloadButton")
        self.download_btn.setFixedWidth(240)
        self.download_btn.setEnabled(False)
        self.download_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.download_btn.clicked.connect(self.download_requested.emit)

        card_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignLeft)
        card_layout.addSpacing(2)
        card_layout.addWidget(self.status_label)
        card_layout.addWidget(self.percentage_label)
        card_layout.addWidget(self.progress_bar)
        card_layout.addSpacing(5)
        card_layout.addWidget(self.download_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch(1)

    def update_progress(self, value: int, status_text: str):
        self.progress_bar.setValue(value)
        self.percentage_label.setText(f"Percentage: {value}%")
        self.status_label.setText(status_text)

    def enable_download(self, file_name: str):
        base_name = file_name.rsplit(".", 1)[0]
        self.download_btn.setText(f"Download {base_name}.txt")
        self.download_btn.setEnabled(True)
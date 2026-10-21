from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton
from core.utils import seleccionar_archivo_audio

class DropView(QWidget):

    audio_selected = pyqtSignal(str)
    continue_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selected_audio_path = ""
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 20, 50, 25)
        main_layout.setSpacing(15)

        main_layout.addStretch(1)

        card = QFrame()
        card.setObjectName("AudioDropCard")
        card.setFixedSize(500, 220)

        card_layout = QVBoxLayout(card)
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.setSpacing(15)

        title = QLabel("Select Audio File")
        title.setObjectName("AudioTitle")

        self.file_label = QLabel("No file selected")
        self.file_label.setObjectName("FileNameLabel")
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        browse_btn = QPushButton("Browse Files")
        browse_btn.setObjectName("ActionButton")
        browse_btn.setFixedWidth(180)
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_btn.clicked.connect(self._on_browse_clicked)

        card_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.file_label, alignment=Qt.AlignmentFlag.AlignCenter)
        card_layout.addSpacing(5)
        card_layout.addWidget(browse_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(15)

        self.continue_btn = QPushButton("Continue")
        self.continue_btn.setObjectName("ContinueButton")
        self.continue_btn.setFixedWidth(180)
        self.continue_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.continue_btn.setEnabled(False)
        self.continue_btn.setStyleSheet(
            "QPushButton#ContinueButton:disabled { background-color: #0e0e10; color: #444448; border-color: #1a1a1e; }"
        )
        self.continue_btn.clicked.connect(self.continue_requested.emit)

        main_layout.addWidget(self.continue_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch(1)

    def _on_browse_clicked(self):
        file_path = seleccionar_archivo_audio(self)
        if file_path:
            self.selected_audio_path = file_path
            file_name = file_path.split("/")[-1].split("\\")[-1]
            
            self.file_label.setText(file_name)

            self.continue_btn.setEnabled(True)
            self.audio_selected.emit(file_path)
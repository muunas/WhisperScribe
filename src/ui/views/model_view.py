from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class ModelView(QWidget):

    model_selected = pyqtSignal(str)
    continue_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selected_model = "small"
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 15, 40, 20)
        main_layout.setSpacing(15)

        row1_layout = QHBoxLayout()
        row1_layout.setSpacing(15)
        row1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        row1_data = [
            ("tiny", "Tiny", "Ultra-fast and basic", "Min RAM: ~0.5 GB", None),
            ("base", "Base", "Lightweight and\nfast", "Min RAM: ~0.8 GB", None),
            (
                "small",
                "Small",
                "Best Balance",
                "Min RAM: ~1.5 GB",
                "(Recommended)",
            ),
        ]

        row2_layout = QHBoxLayout()
        row2_layout.setSpacing(15)
        row2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        row2_data = [
            ("medium", "Medium", "High precision", "Min RAM: ~3.5 GB", None),
            (
                "turbo",
                "Turbo",
                "Maximum speed\nand precision",
                "Min RAM: ~4.5 GB",
                None,
            ),
        ]

        self.card_buttons = {}

        def create_card(key, name, desc, ram, rec):
            card = QPushButton()
            card.setObjectName("ModelCard")
            card.setCheckable(True)
            card.setFixedSize(185, 110)
            card.setCursor(Qt.CursorShape.PointingHandCursor)

            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(12, 10, 12, 10)
            card_layout.setSpacing(3)

            lbl_name = QLabel(name)
            lbl_name.setObjectName("CardTitle")

            lbl_desc = QLabel(desc)
            lbl_desc.setObjectName("CardDesc")
            lbl_desc.setWordWrap(True)

            lbl_ram = QLabel(ram)
            lbl_ram.setObjectName("CardRam")

            card_layout.addWidget(lbl_name)
            card_layout.addWidget(lbl_desc)
            card_layout.addWidget(lbl_ram)

            if rec:
                lbl_rec = QLabel(rec)
                lbl_rec.setObjectName("CardRec")
                card_layout.addWidget(lbl_rec)

            if key == "small":
                card.setChecked(True)

            card.clicked.connect(
                lambda checked, k=key: self._on_card_clicked(k)
            )
            self.card_buttons[key] = card
            return card

        for key, name, desc, ram, rec in row1_data:
            row1_layout.addWidget(create_card(key, name, desc, ram, rec))

        for key, name, desc, ram, rec in row2_data:
            row2_layout.addWidget(create_card(key, name, desc, ram, rec))

        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(12)
        center_layout.addLayout(row1_layout)
        center_layout.addLayout(row2_layout)

        main_layout.addStretch(1)
        main_layout.addWidget(
            center_widget, alignment=Qt.AlignmentFlag.AlignCenter
        )
        main_layout.addSpacing(10)

        self.continue_btn = QPushButton("Continue")
        self.continue_btn.setObjectName("ContinueButton")
        self.continue_btn.setFixedWidth(180)
        self.continue_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.continue_btn.clicked.connect(self.continue_requested.emit)

        main_layout.addWidget(
            self.continue_btn, alignment=Qt.AlignmentFlag.AlignCenter
        )
        main_layout.addStretch(1)

    def _on_card_clicked(self, model_key: str):
        for key, btn in self.card_buttons.items():
            btn.setChecked(key == model_key)
        self.selected_model = model_key
        self.model_selected.emit(model_key)
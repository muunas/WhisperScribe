from pathlib import Path
import sys

"""Facilitamos a python que encuentre la carpeta ui mas facilmente."""
src_dir = Path(__file__).resolve().parent.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

import ctypes
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.styles import STYLE_SHEET
from ui.views.ffmpeg_view import FFmpegView
from ui.views.welcome_view import WelcomeView
from ui.views.model_view import ModelView

def set_dark_title_bar(window):
    if sys.platform == "win32":
        try:
            hwnd = int(window.winId())
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE,
                ctypes.byref(ctypes.c_int(1)),
                ctypes.sizeof(ctypes.c_int),
            )
        except Exception:
            pass


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.selected_model = "small"

        self.setWindowTitle("WhisperScribe")
        self.resize(850, 480)
        self.setMinimumSize(850, 480)
        self.setStyleSheet(STYLE_SHEET)

        root_widget = QWidget()
        root_layout = QVBoxLayout(root_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        header_title = QLabel("WhisperScribe")
        header_title.setObjectName("HeaderTitle")
        header_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        divider = QFrame()
        divider.setObjectName("DividerLine")

        root_layout.addWidget(header_title)
        root_layout.addWidget(divider)


        self.stacked_widget = QStackedWidget()

        self.welcome_view = WelcomeView()
        self.welcome_view.start_requested.connect(self._on_start_clicked)
        self.stacked_widget.addWidget(self.welcome_view)


        self.ffmpeg_view = FFmpegView()
        self.ffmpeg_view.check_finished.connect(self._on_ffmpeg_finished)
        self.stacked_widget.addWidget(self.ffmpeg_view)

        root_layout.addWidget(self.stacked_widget)
        self.setCentralWidget(root_widget)


        self.model_view = ModelView()
        self.model_view.model_selected.connect(self._on_model_selected)
        self.model_view.continue_requested.connect(self._on_continue_clicked)
        self.stacked_widget.addWidget(self.model_view)

    def _on_start_clicked(self):
        self.stacked_widget.setCurrentIndex(1)
        self.ffmpeg_view.start_verification()

    def _on_ffmpeg_finished(self, success: bool):
        if success:
            QTimer.singleShot(1500, self._go_to_model_screen)
        else:
            print("Error en la verificación de FFmpeg.")

    def _go_to_model_screen(self):
        print(
            "FFmpeg verificado -> Listo para cargar la Pantalla 3 (Selector de Modelos)."
        )

    def _go_to_model_screen(self):
        self.stacked_widget.setCurrentIndex(2)

    def _on_model_selected(self, model_key: str):
        self.selected_model = model_key
        print(f"Modelo seleccionado: {self.selected_model}")

    def _on_continue_clicked(self):
        print(f"Continuando con el modelo: {self.selected_model}")
        # self.stacked_widget.setCurrentIndex(3) # Para cuando hagamos la siguiente pantalla


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    set_dark_title_bar(window)
    sys.exit(app.exec())
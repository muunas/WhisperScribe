import sys
import os
from pathlib import Path

"""Facilitamos a python que encuentre la carpeta ui mas facilmente."""
src_dir = Path(__file__).resolve().parent.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

import ctypes
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
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
from ui.views.drop_view import DropView
from ui.views.progress_view import ProgressView
from core.transcription_worker import TranscriptionWorker

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

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
        self.selected_audio = ""

        self.setWindowTitle("WhisperScribe")
        self.resize(850, 480)
        self.setMinimumSize(850, 480)
        self.setStyleSheet(STYLE_SHEET)

        set_dark_title_bar(self)

        icon_path = resource_path("src/assets/app_icon.ico")
        self.setWindowIcon(QIcon(icon_path))

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

        self.model_view = ModelView()
        self.model_view.model_selected.connect(self._on_model_selected)
        self.model_view.continue_requested.connect(self._on_continue_clicked)
        self.stacked_widget.addWidget(self.model_view)

        self.drop_view = DropView()
        self.drop_view.audio_selected.connect(self._on_audio_selected)
        self.drop_view.continue_requested.connect(self._on_audio_continue)
        self.stacked_widget.addWidget(self.drop_view)

        self.progress_view = ProgressView()
        self.stacked_widget.addWidget(self.progress_view)

        root_layout.addWidget(self.stacked_widget)
        self.setCentralWidget(root_widget)

    def _on_start_clicked(self):
        self.stacked_widget.setCurrentIndex(1)
        self.ffmpeg_view.start_verification()

    def _on_ffmpeg_finished(self, success: bool):
        if success:
            QTimer.singleShot(1500, self._go_to_model_screen)
        else:
            print("Error en la verificación de FFmpeg.")

    def _go_to_model_screen(self):
        self.stacked_widget.setCurrentIndex(2)

    def _on_model_selected(self, model_key: str):
        self.selected_model = model_key
        print(f"Modelo seleccionado: {self.selected_model}")

    def _on_continue_clicked(self):
        print(f"Modelo confirmado en MainWindow: {self.selected_model}")
        self.stacked_widget.setCurrentIndex(3) 

    def _on_audio_selected(self, audio_path: str):
        self.selected_audio = audio_path
        print(f"Audio seleccionado: {self.selected_audio}")

    def _on_audio_continue(self):
        print(f"Modelo seleccionado: {self.selected_model}")
        print(f"Audio seleccionado: {self.selected_audio}")
        
        self.stacked_widget.setCurrentIndex(4)
        
        audio_file_name = self.selected_audio.split("/")[-1].split("\\")[-1]
        
        self.progress_view.download_requested.connect(
            lambda: self._handle_download(audio_file_name)
        )
        
        self.worker = TranscriptionWorker(self.selected_model, self.selected_audio)
        self.worker.progress_signal.connect(self.progress_view.update_progress)
        self.worker.finished_signal.connect(lambda text: self._on_transcription_finished(text, audio_file_name))
        self.worker.error_signal.connect(self._on_transcription_error)
        self.worker.start()

    def _on_transcription_finished(self, text: str, audio_file_name: str):
        print("Transcripción finalizada con éxito.")
        self.final_transcript_text = text
        self.progress_view.enable_download(audio_file_name)

    def _handle_download(self, audio_file_name: str):
        from core.utils import guardar_archivo_dialogo
        base_name = audio_file_name.rsplit(".", 1)[0]
        default_name = f"{base_name}_transcription.txt"
        
        saved_path = guardar_archivo_dialogo(self, default_name, self.final_transcript_text)
        if saved_path:
            print(f"Transcripción guardada correctamente en: {saved_path}")

    def _on_transcription_error(self, error_msg: str):
        print(f"Error durante la transcripción: {error_msg}")
        self.progress_view.update_progress(0, f"Error: {error_msg}")
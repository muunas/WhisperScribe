from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal
from core.transcriber import Transcriber, load_audio_with_ffmpeg


class TranscriptionWorker(QThread):
    progress_signal = pyqtSignal(int, str)
    finished_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, model_size: str, audio_path: str):
        super().__init__()
        self.model_size = model_size
        self.audio_path = audio_path

    def run(self):
        try:
            self.progress_signal.emit(10, f"Loading model '{self.model_size}' into the CPU...")
            transcriber = Transcriber(model_name=self.model_size)
            
            file_path = Path(self.audio_path)
            if not file_path.exists():
                self.error_signal.emit(f"File doesn't exist: {self.audio_path}")
                return

            self.progress_signal.emit(30, f"Decoding audio ({file_path.name})...")
            audio_data = load_audio_with_ffmpeg(str(file_path))

            self.progress_signal.emit(45, "Transcribing segments in real-time...")
            
            segments, info = transcriber.model.transcribe(audio_data, beam_size=5)

            text_lines = []
            total_duration = info.duration if info.duration > 0 else 1.0
            has_segments = False

            for segment in segments:
                has_segments = True
                text_lines.append(segment.text)
                
                progress = int((segment.end / total_duration) * 50) + 45
                progress = min(progress, 95)
                
                status_msg = f"Transcribing... [{segment.end:.1f}s / {total_duration:.1f}s]"
                self.progress_signal.emit(progress, status_msg)

            if not has_segments:
                self.finished_signal.emit("No speech detected in the audio file.")
                return

            full_text = " ".join(text_lines).strip()
            self.progress_signal.emit(100, "Transcription completed!")
            self.finished_signal.emit(full_text)

        except Exception as e:
            self.error_signal.emit(str(e))
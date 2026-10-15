from pathlib import Path
import subprocess
from faster_whisper import WhisperModel
import numpy as np


def load_audio_with_ffmpeg(
    file_path: str, sampling_rate: int = 16000
) -> np.ndarray:
    """Convierte cualquier archivo multimedia a un array numérico compatible con Whisper.

    Ejecuta FFmpeg mediante subproceso para extraer el audio en formato Mono a 16 kHz
    y 16-bit PCM directamente en memoria RAM (stdout). Normaliza la señal en un rango
    de [-1.0, 1.0] de tipo float32, evitando la creación de archivos de audio temporales
    en disco.
    """
    cmd = [
        "ffmpeg",
        "-i",
        file_path,
        "-f",
        "s16le",
        "-ac",
        "1",
        "-ar",
        str(sampling_rate),
        "-",
    ]

    process = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True
    )

    return (
        np.frombuffer(process.stdout, dtype=np.int16).astype(np.float32)
        / 32768.0
    )


class Transcriber:

    def __init__(self, model_name: str = "small"):
        self.model_name = model_name

        print(f"Cargando modelo '{self.model_name}' en CPU...")
        self.model = WhisperModel(
            self.model_name, device="cpu", compute_type="int8"
        )
        print("Modelo cargado correctamente en CPU.")

    def transcribe_file(self, audio_path: str) -> str:
        file_path = Path(audio_path)

        if not file_path.exists():
            print(f"Error: El archivo no existe en {audio_path}")
            return ""

        print(f"\nIniciando decodificación de: {file_path.name}")
        audio_data = load_audio_with_ffmpeg(str(file_path))

        print("Iniciando transcripción...\n")
        segments, info = self.model.transcribe(audio_data, beam_size=5)

        print(f"Idioma detectado: {info.language}")
        print(f"Duración: {info.duration:.1f} segundos\n")
        print("--- Progreso ---")

        text_lines = []

        for segment in segments:
            progress = (
                (segment.end / info.duration) * 100 if info.duration > 0 else 0
            )
            print(
                f"[{progress:.0f}%] {segment.start:.1f}s -> {segment.end:.1f}s: {segment.text}"
            )
            text_lines.append(segment.text)

        print("----------------")
        return " ".join(text_lines)
from pathlib import Path
import sys

"""
Configuración del entorno de importaciones:
Añade el directorio padre al 'sys.path' para permitir la resolución dinámica
de módulos internos de la carpeta 'core' (evita errores de ModuleNotFoundError
independientemente desde dónde se ejecute el script).
"""
sys.path.append(str(Path(__file__).resolve().parent))

from core.ffmpeg_checker import ensure_ffmpeg
from core.transcriber import Transcriber
from core.utils import guardar_transcripcion

NOMBRE_AUDIO = "TestRecording.m4a"

def main():

    root_folder = Path(__file__).resolve().parent.parent
    audios_folder = root_folder / "audios"
    audio_path = audios_folder / NOMBRE_AUDIO

    print("[1/3] Verificando FFmpeg...")
    if not ensure_ffmpeg():
        print("No se pudo inicializar FFmpeg. Revisa la conexión a internet.")
        sys.exit(1)

    print("FFmpeg listo.")


    if not audio_path.exists():
        print(f"\nError: No se encontró el archivo '{NOMBRE_AUDIO}'")
        print(f"Ruta buscada: {audio_path}")
        print("Asegúrate de colocar tu archivo dentro de la carpeta 'audios/'.")
        return

    print("\n[2/3] Inicializando Whisper...")
    try:
        transcriber = Transcriber()
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return

    print(f"\n[3/3] Procesando audio: {audio_path.name}...")
    resultado = transcriber.transcribe_file(str(audio_path))

    if resultado:
        ruta_guardada = guardar_transcripcion(audio_path.name, resultado)
        print(f"\nTranscripción completa. Guardada en: {ruta_guardada}")


if __name__ == "__main__":
    main()
from pathlib import Path
from PyQt6.QtWidgets import QFileDialog

def guardar_transcripcion(ruta_audio: str, texto: str) -> Path:
    raiz_proyecto = Path(__file__).resolve().parent.parent.parent
    carpeta_destino = raiz_proyecto / "Transcriptions"

    carpeta_destino.mkdir(exist_ok=True)


    nombre_audio = Path(ruta_audio).stem
    ruta_txt = carpeta_destino / f"{nombre_audio}.txt"


    with open(ruta_txt, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    return ruta_txt

def seleccionar_archivo_audio(parent=None) -> str:
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Seleccionar archivo de audio",
        "",
        "Archivos multimedia (*.mp3 *.wav *.m4a *.mp4 *.flac *.ogg);;Todos los archivos (*.*)",
    )
    return file_path

from PyQt6.QtWidgets import QFileDialog

def guardar_archivo_dialogo(parent, default_filename: str, content: str) -> str:
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Guardar transcripción",
        default_filename,
        "Archivos de texto (*.txt);;Todos los archivos (*.*)"
    )
    
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return file_path
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
    return ""


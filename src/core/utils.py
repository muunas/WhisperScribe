from pathlib import Path


def guardar_transcripcion(ruta_audio: str, texto: str) -> Path:
    raiz_proyecto = Path(__file__).resolve().parent.parent.parent
    carpeta_destino = raiz_proyecto / "Transcriptions"

    carpeta_destino.mkdir(exist_ok=True)


    nombre_audio = Path(ruta_audio).stem
    ruta_txt = carpeta_destino / f"{nombre_audio}.txt"


    with open(ruta_txt, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    return ruta_txt


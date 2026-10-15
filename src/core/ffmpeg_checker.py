import json
import os
from pathlib import Path
import sys
import urllib.request
import zipfile


"""Pipeline:
    1. Comprobación: Verifica si 'ffmpeg.exe' ya existe en la carpeta 'bin/'
    añadiéndola al PATH del sistema.
    2. Consulta de API: Si no existe, pide a la API de GitHub la URL del paquete más reciente.
    3. Descarga y extracción: Descarga el ZIP oficial en memoria, extrae ÚNICAMENTE el
       ejecutable 'ffmpeg.exe' dentro de 'bin/' y elimina el ZIP temporal.
    4. Registro: Añade la carpeta 'bin/' al PATH activo para la sesión.
    """

def ensure_ffmpeg() -> bool:
    bin_folder = Path(__file__).resolve().parent.parent.parent / "bin"
    bin_folder.mkdir(exist_ok=True)

    exe_name = "ffmpeg.exe" if sys.platform == "win32" else "ffmpeg"
    ffmpeg_path = bin_folder / exe_name

    if ffmpeg_path.exists():
        os.environ["PATH"] = (
            f"{bin_folder}{os.pathsep}{os.environ.get('PATH', '')}"
        )
        return True

    print("FFmpeg no encontrado en 'bin/'. Descargando versión más reciente...")

    try:
        api_url = (
            "https://api.github.com/repos/BtbN/FFmpeg-Builds/releases/latest"
        )
        req = urllib.request.Request(
            api_url, headers={"User-Agent": "WhisperScribe"}
        )

        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())

        download_url = next(
            (
                asset["browser_download_url"]
                for asset in data.get("assets", [])
                if asset["name"].endswith("win64-gpl.zip")
            ),
            None,
        )

        if not download_url:
            print("No se encontró el paquete de FFmpeg en GitHub.")
            return False

        zip_path = bin_folder / "ffmpeg.zip"
        urllib.request.urlretrieve(download_url, zip_path)

        with zipfile.ZipFile(zip_path, "r") as zip_file:
            for item in zip_file.namelist():
                if item.endswith(exe_name):
                    with (
                        zip_file.open(item) as src,
                        open(ffmpeg_path, "wb") as dst,
                    ):
                        dst.write(src.read())
                    break

        zip_path.unlink()

        os.environ["PATH"] = (
            f"{bin_folder}{os.pathsep}{os.environ.get('PATH', '')}"
        )
        print("FFmpeg descargado e instalado correctamente.")
        return True

    except Exception as e:
        print(f"Error al obtener FFmpeg: {e}")
        return False
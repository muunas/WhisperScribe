STYLE_SHEET = """
QMainWindow {
    background-color: #18181a;
}

QWidget {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    color: #e5e5e7;
}

/* Cabecera superior */
QLabel#HeaderTitle {
    font-size: 28px;
    font-weight: bold;
    font-style: italic;
    color: #6320ee;
    padding-top: 6px;
    padding-bottom: 6px;
}

/* Línea morada divisora horizontal */
QFrame#DividerLine {
    background-color: #6320ee;
    border: none;
    max-height: 2px;
    min-height: 2px;
}

/* Título de sección / Welcome */
QLabel#SectionTitle {
    font-size: 26px;
    font-weight: bold;
    font-style: italic;
    color: #6320ee;
    margin-bottom: 10px;
}

/* Texto descriptivo de cuerpo */
QLabel#BodyText {
    font-size: 15px;
    font-style: italic;
    color: #d1d1d6;
    line-height: 1.45;
}

/* Botón principal de acción */
QPushButton#ActionButton {
    background-color: #121214;
    color: #6320ee;
    font-size: 22px;
    font-weight: bold;
    font-style: italic;
    border: 1px solid #28282c;
    border-radius: 10px;
    padding: 14px 0px;
}

QPushButton#ActionButton:hover {
    background-color: #202024;
    border-color: #6320ee;
}

QPushButton#ActionButton:pressed {
    background-color: #0a0a0c;
}

/* Subtexto descriptivo para la pantalla de FFmpeg */
QLabel#SubStatusText {
    font-size: 14px;
    font-style: italic;
    color: #9898a0;
}
"""
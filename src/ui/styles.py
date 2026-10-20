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

/* Tarjetas de Modelos (Cuadrícula) */
QPushButton#ModelCard {
    background-color: #141416;
    border: 1px solid #28282c;
    border-radius: 12px;
    text-align: left;
    padding: 16px;
}

QPushButton#ModelCard:hover {
    background-color: #1c1c21;
    border-color: #6320ee;
}

QPushButton#ModelCard:checked {
    background-color: #1c1c24;
    border: 2px solid #6320ee;
}

/* Tipografía de las tarjetas */
QLabel#CardTitle {
    font-size: 18px;
    font-weight: bold;
    font-style: italic;
    color: #6320ee;
}

QLabel#CardDesc {
    font-size: 13px;
    font-style: italic;
    color: #d1d1d6;
}

QLabel#CardRam {
    font-size: 12px;
    font-style: italic;
    color: #9898a0;
}

QLabel#CardRec {
    font-size: 12px;
    font-style: italic;
    font-weight: bold;
    color: #6320ee;
}

/* Botón Continue */
QPushButton#ContinueButton {
    background-color: #121214;
    color: #6320ee;
    font-size: 18px;
    font-weight: bold;
    font-style: italic;
    border: 1px solid #28282c;
    border-radius: 10px;
    padding: 10px 30px;
}

QPushButton#ContinueButton:hover {
    background-color: #202024;
    border-color: #6320ee;
}

QPushButton#ContinueButton:pressed {
    background-color: #0a0a0c;
}
"""
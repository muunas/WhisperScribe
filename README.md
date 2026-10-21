# WhisperScribe

> Transcripciones de audio locales, ultra-rápidas, 100% gratuitas y con privacidad absoluta. Olvídate de las suscripciones en la nube y las tarifas por minuto.

---

## El Problema

En la actualidad, procesar voz a texto con alta precisión suele implicar contrapartidas frustrantes:
1. **Costes ocultos y suscripciones:** Los servicios líderes en la nube cobran por minuto transcrito, lo que penaliza proyectos personales o flujos de trabajo con grandes volúmenes de audio.
2. **Brechas de privacidad:** Enviar archivos de audio personales, reuniones corporativas o entrevistas sensibles a servidores de terceros vulnera la confidencialidad de los datos.
3. **Infierno de configuración:** Las soluciones locales basadas en IA suelen requerir configuraciones avanzadas de hardware, tarjetas gráficas dedicadas (NVIDIA/CUDA) y dependencias de C++ muy frágiles que se rompen constantemente en entornos de escritorio (especialmente en Windows).

---

## La Solución: WhisperScribe

**WhisperScribe** democratiza el acceso a la tecnología de transcripción de vanguardia de OpenAI (`Whisper`) empaquetándola en una aplicación de escritorio nativa, moderna y elegante. 

Está diseñada bajo una premisa clara: **ejecutarse íntegramente en tu propia máquina (Local-First)**, aprovechando la optimización extrema de `faster-whisper` para ofrecer resultados profesionales sin coste, sin conexión a internet obligatoria y con **cero fugas de datos**.

---

## Características Principales

*   **100% Gratuito y Sin Límites:** Sin pasarelas de pago, registros ni restricciones en la duración o cantidad de archivos que procesas.
*   **Privacidad Absoluta:** Tus datos nunca abandonan tu disco duro. Ideal para periodistas, desarrolladores, investigadores y profesionales que manejan información confidencial.
*   **Diseño Moderno e Interfaz Fluida (PyQt6):** Una UI minimalista en modo oscuro diseñada desde cero (con prototipado previo en Figma), que guía al usuario paso a paso sin saturarlo.
*   **Procesamiento Asíncrono Real (`QThreads`):** La interfaz nunca se congela. Un hilo secundario gestiona la IA mientras la barra de progreso y los estados se actualizan en tiempo real.
*   **Ingesta Eficiente de Audio:** Mediante una arquitectura de tuberías con subprocesos de FFmpeg, el audio se decodifica directamente en la memoria RAM, evitando saturar el almacenamiento con archivos temporales en disco.
*   **Exportación Nativa:** Guarda el resultado limpio de tus transcripciones en formato `.txt` con un solo clic a través del explorador de archivos nativo de tu sistema.

---

## Decisiones de Ingeniería y Robustez

Como software diseñado para perdurar en el tiempo y evitar obsolescencias imprevistas, WhisperScribe implementa los siguientes estándares técnicos:

*   **Estrategia CPU-First con Cuantización `int8`:** Por defecto, el motor prioriza la ejecución optimizada en CPU utilizando cuantización de 8 bits. Esto garantiza una estabilidad total en Windows, eliminando los clásicos dolores de cabeza de las DLLs faltantes de CUDA sin sacrificar velocidad de manera perceptible.
*   **Control estricto de dependencias:** Las versiones clave (como `faster-whisper`, `av` y `PyQt6`) están congeladas en el entorno para prevenir rupturas provocadas por actualizaciones automáticas de terceros.
*   **Arquitectura Modular:** Separación estricta de responsabilidades entre la capa de presentación (`ui/views`), el orquestador de la ventana principal (`ui/main_window.py`), los hilos de computación (`core/worker.py`) y el motor de IA (`core/transcriber.py`).

## Stack Tecnológico
*   **Python 3.10+ (Core logic)**

*   **PyQt6 (Framework de interfaz gráfica de usuario nativa)**

*   **faster-whisper (Implementación optimizada de CTranslate2 para los modelos de OpenAI)**

*   **FFmpeg (Procesamiento multimedia en segundo plano)**
  
## Licencia

Este proyecto se distribuye bajo la licencia MIT. Siéntete libre de usarlo, modificarlo y adaptarlo a tus necesidades.

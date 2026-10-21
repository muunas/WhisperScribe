# WhisperScribe

> Local, ultra-fast, 100% free audio transcriptions with absolute privacy. Forget about cloud subscriptions and per-minute fees.

---

## The Problem

Today, high-accuracy speech-to-text processing often comes with frustrating trade-offs:
1. **Hidden costs and subscriptions:** Leading cloud services charge per transcribed minute, punishing personal projects or workflows involving large volumes of audio.
2. **Privacy risks:** Sending personal audio files, corporate meetings, or sensitive interviews to third-party servers compromises data confidentiality.
3. **Configuration headaches:** Local AI solutions usually require complex hardware setups, dedicated graphics cards (NVIDIA/CUDA), and fragile C++ dependencies that constantly break on desktop environments (especially Windows).

---

## The Solution: WhisperScribe

**WhisperScribe** democratizes access to OpenAI's state-of-the-art transcription technology (`Whisper`) by packaging it into a native, modern, and sleek desktop application.

It is built on a clear premise: **run entirely on your local machine (Local-First)**, leveraging the extreme optimization of `faster-whisper` to deliver professional-grade results with zero cost, no mandatory internet connection, and **zero data leaks**.

---

## Key Features

*   **100% Free and Unlimited:** No paywalls, mandatory accounts, or limits on audio duration or file count.
*   **Absolute Privacy:** Your data never leaves your hard drive. Ideal for journalists, developers, researchers, and professionals handling sensitive information.
*   **Modern Design and Smooth UI (PyQt6):** A minimalist dark-mode interface designed from scratch (prototyped in Figma) that guides the user step by step without clutter.
*   **True Asynchronous Processing (`QThreads`):** The interface never freezes. A background thread runs the AI engine while progress bars and status labels update in real time.
*   **Efficient Audio Ingestion:** Powered by FFmpeg subprocess pipelines, audio is decoded directly into RAM, preventing disk clutter from temporary files.
*   **Native Export:** Save your clean transcription text files (`.txt`) with a single click using your system's native file dialog.

---

## Engineering and Robustness Decisions

Built to last and avoid unexpected breakage over time, WhisperScribe incorporates the following technical standards:

*   **CPU-First Strategy with `int8` Quantization:** By default, the engine prioritizes optimized execution on CPU using 8-bit quantization. This guarantees rock-solid stability on Windows by eliminating CUDA DLL dependencies without noticeable speed penalties.
*   **Strict Dependency Control:** Key package versions (such as `faster-whisper`, `av`, and `PyQt6`) are pinned to prevent breaking changes caused by automatic third-party updates.
*   **Modular Architecture:** Strict separation of concerns between presentation layers (`ui/views`), window orchestration (`ui/main_window.py`), worker threads (`core/worker.py`), and the underlying AI engine (`core/transcriber.py`).

---

## Tech Stack

*   **Python 3.10+** (Core logic and workflow control)
*   **PyQt6** (Native desktop GUI framework)
*   **faster-whisper** (Optimized CTranslate2 engine for OpenAI Whisper models)
*   **FFmpeg** (Background multimedia processing and stream extraction)

---

## License

This project is distributed under the **MIT License**. Feel free to use, modify, and adapt it to your needs.

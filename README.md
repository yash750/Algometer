# Algometer

**Algometer** is an intelligent tool for evaluating student algorithm assignments using a tuned version of the Gemini model. It accepts `.txt` and image files (`.jpg`, `.jpeg`, `.png`) and outputs a JSON response with:

- `status`: Correctness (`True`/`False`).
- `feedback`: Comments and suggestions.

## Features

- Supports multiple formats (text & image).
- Personalized evaluation feedback.
- Consistent assessment for diverse algorithm styles.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/algometer.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```

## Usage

Upload `.txt` or image files through the web interface. Algometer evaluates and returns feedback on the submission.

## Technologies Used

- **Flask**: Web server.
- **Tesseract OCR**: Text extraction from images.
- **Gemini Model**: Evaluating algorithm correctness.

## Contributing

Contributions are welcome via Pull Requests.

## License

MIT License.

---

*Algometer - Intelligent Evaluation for Student Algorithms.*


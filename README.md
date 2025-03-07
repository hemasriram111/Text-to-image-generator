# Tkinter FastAPI Image Generator

This project is a simple GUI application built with Tkinter and FastAPI that allows users to generate AI-generated images using the Hugging Face API. The user inputs a prompt, and the system returns an image based on that prompt.

## Features
- User-friendly Tkinter GUI
- AI-powered image generation via Hugging Face API
- CustomTkinter for a modern UI experience
- Display generated images within the application

## Requirements
To run this project, install the required dependencies using:

```sh
pip install -r requirements.txt
```

## Installation and Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/tkinter-fastapi-image-generator.git
   cd tkinter-fastapi-image-generator
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python app.py
   ```

## API Key Configuration
Replace the `API_KEY` variable inside `app.py` with your actual Hugging Face API key:
```python
API_KEY = "your_huggingface_api_key"
```

## Dependencies
The required packages are listed in `requirements.txt` and include:
- `tkinter`
- `customtkinter`
- `Pillow`
- `requests`

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Hugging Face API for AI image generation
- CustomTkinter for the enhanced UI


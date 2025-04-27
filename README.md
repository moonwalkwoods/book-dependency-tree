# Book Dependency Tree

This project generates a dependency tree of intellectual influences for a given book, tracing the lineage of cited works and bibliographies recursively. It uses OpenAI's GPT-4 API to analyze and build a directory-style hierarchy of sources that influenced the selected book.

## Features
- Enter a book title and author to generate a dependency graph.
- Visualizes the intellectual lineage in a directory-style tree.
- Web interface for easy use.

## How It Works
- The backend (Flask) receives a book title and author, then queries the OpenAI API to generate a dependency tree.
- The frontend (HTML/JS) allows users to input book details and view the generated tree.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/moonwalkwoods/dependency-nest.git
   cd dependency-nest
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory with your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the server:**
   ```sh
   python app.py
   ```
   The server will start on `http://localhost:8002`.

5. **Open the web interface:**
   - Open `index.html` in your browser, or navigate to `http://localhost:8002` if served directly.

## Usage
1. Enter the book title and author in the input fields.
2. Click **Generate Graph**.
3. View the generated dependency tree in the output area.

## Requirements
- Python 3.8+
- Flask
- Flask-CORS
- openai
- dotenv

## License
GNU GENERAL PUBLIC LICENSE 
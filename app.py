import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/generate_tree', methods=['POST'])
def generate_tree():
    try:
        data = request.json
        book_title = data.get('book_title')
        author = data.get('author')

        if not book_title or not author:
            return jsonify({'error': 'Book title and author are required'}), 400

        prompt = (
            f"Build a dependency graph for a book, where you take all mentions of other books and sources used and those are the dependencies of the original book, then take the sources used for those books and continue on."
            f"Can you do this for the book '{book_title}' by {author}?"
            f"For each dependency, recursively list their own dependencies, at least 2 levels deep."
            f"Examine the bibliographies and cited works within the texts of these influential figures, tracing the lineage of ideas further back. This recursive approach would map the evolution of revolutionary thought leading up to '{book_title}' by {author}."
            f"Output thedependency graph expanded into a directory-style hierarchy, clearly illustrating the lineage of intellectual influences leading to '{book_title}' by {author}."
            f"The root will be '{book_title}' by {author}. and then the dependencies will be branches, and then those dependencies' dependencies will be subbranches in the tree."
            f"Output only the directory structure and nothing else."

        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        tree_text = response.choices[0].message.content.strip()
        return jsonify({'tree': tree_text})

    except Exception as e:
        print(f"Error: {str(e)}")  # This will help us see the error in the server logs
        error_message = str(e)
        if "insufficient_quota" in error_message:
            return jsonify({
                'error': 'OpenAI API quota has been exceeded. Please try again later or contact the administrator.'
            }), 500
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=False)

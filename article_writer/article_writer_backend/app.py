from flask import Flask, request, jsonify
from flask_cors import CORS
from services.chat_service import initiate_chat
import json
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate_article', methods=['POST'])
def generate_article():
    problem = request.json.get('problem', '')
    if not problem:
        return jsonify({"error": "Problem statement is required"}), 400

    try:
        article = initiate_chat(problem)
        print("=========================================================")
        print(article)
        return jsonify(article), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
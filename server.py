"""
Flask application for emotion detection using a sentiment analysis model.
"""

import os
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Flask app configuration
app = Flask(
    __name__,
    template_folder="oaqjp-final-project-emb-ai/templates",
    static_folder="oaqjp-final-project-emb-ai/static",
)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect the dominant emotion in a given text statement.

    Returns:
        JSON: A JSON response containing the formatted result or an error message.
    """
    try:
        # Validate input
        data = request.json
        if not data or not data.get("statement", "").strip():
            return jsonify({"message": "Invalid text! Please try again!"}), 400

        # Get the input statement
        statement = data.get("statement", "").strip()

        # Process the statement using the emotion detector
        result = emotion_detector(statement)

        # Check if the result is empty or None
        if result['dominant_emotion'] is None:
            return jsonify({"message": "Invalid text! Please try again!"}), 400

        # Format the response
        formatted_response = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion is "
            f"{result['dominant_emotion']}."
        )

        return jsonify({"message": formatted_response})

    except ValueError as error:
        return jsonify({"message": f"An error occurred: {str(error)}"}), 500

@app.route('/')
def home():
    """
    Render the home page of the application.

    Returns:
        HTML: Rendered index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    print("Flask is running from:", os.getcwd())
    app.run(host="0.0.0.0", port=8080)

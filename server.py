"""
Flask Application for Emotion Detection
"""

import json
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the given text and returns the detected emotions.

    Returns:
        str: Formatted response string or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_json = emotion_detector(text_to_analyze)
    response = json.loads(response_json)

    if response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

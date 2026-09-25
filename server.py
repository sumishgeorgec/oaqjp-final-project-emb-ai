"""
    Emotion Detection web server

    It runs a Flask web application to detect emotions from a text
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyse the query string and extract the emotion scores and dominant emotion
    """
    # Retrieve the text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Retrieve the emotions in text_to_analyze
    response = emotion_detector(text_to_analyze)
    return_string = "Invalid text! Please try again!."
    if response['dominant_emotion'] is not None:
        return_string =  (
                f"For the given statement, the system response is 'anger': {response['anger']}, "
                f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
                f"'joy': {response['joy']} and 'sadness': {response['sadness']}. The"
                f" dominant emotion is {response['dominant_emotion']}"
                )
    return return_string

@app.route("/")
def render_index_page():
    """
    Render the index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

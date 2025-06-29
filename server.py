'''
This server is for testing my knowlage
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_analyzer():
    '''
    This function retuns emotion analysis
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Test if some key (in this key "joy") is "None"
    if response.get("joy") is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the prescripted text
    #emotion_list = [f"{name}: {score}" for name, score in response.items()
    # if name != "dominant_emotion"]
    emotion_list = [
    f"{name}: {score}"
    for name, score in response.items()
    if name != "dominant_emotion"
    ]
    emotion_str = ", ".join(emotion_list)
    dominant = response.get("dominant_emotion", "not available")

    return (
        f"For the given statement, the system detected the following emotions: "
        f"{emotion_str}. The dominant emotion is: {dominant}."
    )
@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

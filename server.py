''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector() function.
        The output is then returned formatted as required by the customer.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)
    
    dominant_emotion = response.get('dominant_emotion')
    
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
        
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
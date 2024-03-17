from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.json
    text_to_analyze = data['text']
    print(text_to_analyze)
    result = emotion_detector(text_to_analyze)
    
 
    output_text = "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(
        result['anger'], result['disgust'], result['fear'], result['joy'], result['sadness'], result['dominant_emotion'])
    
    return output_text

if __name__ == '__main__':
    app.run(debug=True)

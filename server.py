from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.json
    text_to_analyze = data['text']
    
    result = emotion_detector(text_to_analyze)
    
    response = {
        "anger": result['anger'], 
        "disgust": result['disgust'], 
        "fear": result['fear'], 
        "joy": result['joy'], 
        "sadness": result['sadness'], 
        "dominant_emotion": result['dominant_emotion']
    }
    
    output_text = "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(
        result['anger'], result['disgust'], result['fear'], result['joy'], result['sadness'], result['dominant_emotion'])
    
    return jsonify(response), output_text

if __name__ == '__main__':
    app.run(debug=True)

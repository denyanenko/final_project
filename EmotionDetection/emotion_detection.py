import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
       
        response_dict = json.loads(response.text)

        emotion_predictions = response_dict['emotionPredictions']
        emotions_dict = emotion_predictions[0]['emotion']

        anger_score = emotions_dict['anger']
        disgust_score = emotions_dict['disgust']
        fear_score = emotions_dict['fear']
        joy_score = emotions_dict['joy']
        sadness_score = emotions_dict['sadness']
        
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return output
    else:
        return "Error"

import json  
class EmotionDetectionService:
    def detect_emotion(self, text):
        simulated_response = json.dumps({
            'anger': 0.1,
            'disgust': 0.05,
            'fear': 0.2,
            'joy': 0.6,
            'sadness': 0.05
        })
        return type('Response', (object,), {"text": simulated_response})()
def emotion_detector(text_to_analyze):
    service = EmotionDetectionService()
    response = service.detect_emotion(text_to_analyze)
    response_dict = json.loads(response.text)
    emotions = {
        'anger': response_dict.get('anger', 0),
        'disgust': response_dict.get('disgust', 0),
        'fear': response_dict.get('fear', 0),
        'joy': response_dict.get('joy', 0),
        'sadness': response_dict.get('sadness', 0)
    }
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

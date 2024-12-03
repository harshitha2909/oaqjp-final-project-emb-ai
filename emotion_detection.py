# Mock Emotion Detection Function
class EmotionDetectionService:
    def detect_emotion(self, text):
        if "love" in text.lower():
            return type('Response', (object,), {"text": "Joy"})()
        else:
            return type('Response', (object,), {"text": "Neutral"})()

# Function to Run Emotion Detection
def emotion_detector(text_to_analyze):
    service = EmotionDetectionService()
    response = service.detect_emotion(text_to_analyze)
    return response.text



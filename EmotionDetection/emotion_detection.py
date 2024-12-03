import json

def emotion_detector(text):
    if not text.strip():  # Check if the input is blank
        # Return the dictionary with all keys set to None for blank inputs
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text = text.lower()
    if "hate" in text or "angry" in text:
        simulated_response = json.dumps({
            'anger': 0.8,
            'disgust': 0.1,
            'fear': 0.05,
            'joy': 0.01,
            'sadness': 0.04
        })
    elif "love" in text or "happy" in text:
        simulated_response = json.dumps({
            'anger': 0.05,
            'disgust': 0.02,
            'fear': 0.01,
            'joy': 0.9,
            'sadness': 0.02
        })
    else:
        simulated_response = json.dumps({
            'anger': 0.1,
            'disgust': 0.05,
            'fear': 0.2,
            'joy': 0.3,
            'sadness': 0.35
        })

    # Parse JSON response and find dominant emotion
    response = json.loads(simulated_response)
    response['dominant_emotion'] = max(response, key=response.get)
    return response  # Removed tuple, returning only dictionary

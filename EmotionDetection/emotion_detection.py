import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Handle blank input before making a request
    if not text_to_analyse or text_to_analyse.strip() == "":
        return json.dumps({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        })

    myobj = {"raw_document": {"text": text_to_analyse}}
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format

        # Extracting emotions
        emotions = data["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)  # Finding dominant emotion

        # Formatting output
        formatted_output = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

        return json.dumps(formatted_output)

    elif response.status_code == 400:  # Handling 400 status code
        return json.dumps({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        })

    else:
        return json.dumps({
            "error": "Failed to fetch emotions",
            "status_code": response.status_code
        }, indent=4)

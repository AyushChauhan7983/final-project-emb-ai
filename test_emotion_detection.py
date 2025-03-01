import unittest
import json
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = json.loads(emotion_detector('I am glad this happened'))
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = json.loads(emotion_detector('I am really mad about this'))
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = json.loads(emotion_detector('I am so sad about this'))
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        result5 = json.loads(emotion_detector('I am really afraid that this will happen'))
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_dominant_emotion in test_cases:
            with self.subTest(text=text):
                emotion_scores = emotion_detector(text)
                # emotion with highest score
                detected_dominant = max(emotion_scores, key=emotion_scores.get)
                self.assertEqual(
                    detected_dominant, expected_dominant_emotion,
                    f"Text: '{text}' should be '{expected_dominant_emotion}', but it was detected '{detected_dominant}'"
                )

if __name__ == "__main__":
    unittest.main()
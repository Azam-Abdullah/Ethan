import os
import subprocess
import requests
import pygame
from dotenv import load_dotenv

load_dotenv()
DG_API_KEY = os.getenv("DEEPGRAM_API_KEY")
class TextToSpeech:
    # DG_API_KEY = "8c6d8a7a804547b4ef296eced5771b07dc721b1a"
    MODEL_NAME = "aura-helios-en"  # Change as needed
    # print(f"{os.getenv('DEEPGRAM_API_KEY')}")

    def __init__(self):
        pygame.mixer.init()

    def speak(self, text):
        DEEPGRAM_URL = f"https://api.deepgram.com/v1/speak?model={self.MODEL_NAME}&encoding=linear16&sample_rate=24000"
        headers = {
            "Authorization": f"Token {DG_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {"text": text}
        response = requests.post(DEEPGRAM_URL, headers=headers, json=payload, stream=True)
        
        if response.status_code == 200:
            # Save the audio to a WAV file
            temp_audio_path = "output.wav"
            with open(temp_audio_path, "wb") as audio_file:
                audio_file.write(response.content)

            # Play the audio using pygame
            self.play_audio(temp_audio_path)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    def play_audio(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the sound has finished playing
            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    tts = TextToSpeech()
    paragraph = """In the quiet moments before dawn, the world seemed suspended in a tranquil hush,
                   as if time itself had paused to catch its breath."""
    
    print(f"Speaking: {paragraph}")
    tts.speak(paragraph)

from gtts import gTTS
import os

def speak_text(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("speech.mp3")

speak_text("Hello! I am here to help you.")
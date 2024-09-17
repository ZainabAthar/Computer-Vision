from gtts import gTTS #gTTS (Google Text-to-Speech) is a library that converts text into speech
import os #interact with the operating system

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("response.mp3")
    os.system("start response.mp3")  # Use 'start' command to play audio on Windows

if __name__ == "__main__":
    text_to_speech("Hello, how are you?", "en")

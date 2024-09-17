import speech_recognition as sr #recognizing speech from audio files
from langdetect import detect #detecting the language of a given text

def recognize_speech_and_detect_language(audio_file):
    recognizer = sr.Recognizer() #creation of object
    with sr.AudioFile(audio_file) as source: #open the audio file
        audio = recognizer.record(source) #record audio
    text = recognizer.recognize_google(audio) #Uses Google's Web Speech API to recognize the speech in the audio and convert it to text
    language = detect(text)
    return text, language
if __name__ == "__main__":
    text, language = recognize_speech_and_detect_language("Sports.wav")
    print(f"Recognized text: {text}")
    print(f"Detected language: {language}")

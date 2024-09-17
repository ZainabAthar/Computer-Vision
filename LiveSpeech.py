import speech_recognition as sr
from langdetect import detect

def recognize_speech_live(): #captures live audio from the microphone, recognizes the speech, and detects the language
    recognizer = sr.Recognizer() ##Creates a Recognizer object.
    mic = sr.Microphone() #Creates a Microphone object for capturing audio.
    try:
        with mic as source:  #Opens the microphone as the audio source.
            recognizer.adjust_for_ambient_noise(source) #Adjusts the recognizer sensitivity to ambient noise levels
            print("Listening...")
            audio = recognizer.listen(source) 
        print("Audio recorded.")
        text = recognizer.recognize_google(audio) #Google’s Web Speech API and converts it to text
        print("Speech recognized.")
        language = detect(text)
        print("Language detected.")
        return text, language
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        result = recognize_speech_live()
        if result:
            text, language = result
            print(f"Recognized text: {text}")
            print(f"Detected language: {language}")
    except Exception as e:
        print(f"An error occurred: {e}")

import cv2
import mediapipe as mp
import speech_recognition as sr
import pyttsx3  # For text-to-speech synthesis

def recognize_faces(video_source=0):
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture
    video_capture = cv2.VideoCapture(video_source)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                # Draw bounding box and label on the frame
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def recognize_speech_live():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        language = 'en'  # This is a placeholder; Google Speech Recognition always returns English
        return text, language
    except sr.UnknownValueError:
        return "Sorry, I did not understand that.", 'en'
    except sr.RequestError as e:
        return f"Sorry, there was an error: {e}", 'en'

def text_to_speech(text, language='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)  # Volume 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

def virtual_assistant():
    while True:
        text, language = recognize_speech_live()
        print(f"Recognized Text: {text}, Language: {language}")
        
        # Recognize faces in real-time
        recognize_faces()
        
        # Respond with speech synthesis
        response_text = f"You said: {text}"
        text_to_speech(response_text, language)

        # Break the loop if needed
        if 'exit' in text.lower():
            break

virtual_assistant()

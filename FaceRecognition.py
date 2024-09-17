import cv2 #OpenCV library for computer vision tasks
import mediapipe as mp #Google developed Library for ML and CV
 
def recognize_faces(video_source=0): #0 == default camera
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection #Accesses MediaPipe's face detection module
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture
    video_capture = cv2.VideoCapture(video_source)
 
    while True: #infinite loop for continuous video processing
        ret, frame = video_capture.read() #Reads a frame from the video source. 
        if not ret: #ret is a boolean indicating if the frame was successfully read
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                #relative to absolute pixels based on frame's dimensions
                # Draw bounding box and label on the frame
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

recognize_faces()

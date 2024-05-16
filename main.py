import cv2
import face_recognition
from datetime import datetime
from recognizer import load_known_faces, mark_attendance
cap = cv2.VideoCapture(0)
cap.set(3, 1280) 
cap.set(4, 720)   

KNOWN_FACES_DIR = "known_faces"
date = datetime.now().strftime('%Y-%m-%d')
attendance_file = f'{date}_attendance.csv'
f = open(attendance_file, 'a+') 
f.close()

FACE_RECOGNITION_THRESHOLD = 0.6

known_faces, known_names = load_known_faces(KNOWN_FACES_DIR)

while True:
    ret, frame = cap.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=FACE_RECOGNITION_THRESHOLD)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            mark_attendance(attendance_file, name)

        # Draw a rectangle and put text on the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow("Face Recognition", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

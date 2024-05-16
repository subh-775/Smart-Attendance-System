from datetime import datetime
import face_recognition
import os

# Function to mark attendance
def mark_attendance(attendance_file, name):
    with open(attendance_file, "a+") as file:
        file.seek(0)
        lines = file.readlines()
        attendance_list = [line.split(",")[0] for line in lines]

        if name not in attendance_list:
            file.write(f"{name},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Function to get encoding for a given image
def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)

    return face_encodings[0] if face_encodings else None

# Function to load known faces and their names
def load_known_faces(known_faces_dir):
    known_faces = []
    known_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg"):
            path = os.path.join(known_faces_dir, filename)
            name = os.path.splitext(filename)[0]
            encoding = get_face_encoding(path)

            if encoding is not None:
                known_faces.append(encoding)
                known_names.append(name)
            else:
                print(f"Warning: Unable to recognize face in {filename}")

    return known_faces, known_names

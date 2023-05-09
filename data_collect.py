import cv2
import os
import face_recognition
import numpy as np

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0 
known_face_encodings = [
    
]
known_face_names = [
    
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def register_someone():

    per_to_recog =str(input("你的名字 : ")).upper()

   

    if existe:
        print("Esta persona ya existe")
        per_to_recog = str(input("Nuevo nombre: "))

    else:
        take_foto()

def take_foto():
    face_recognition.load_image_file()

def video_start():

    while True:
        ret, frame =video.read()
        faces =facedetect.detectMultiScale(frame,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),3)

        cv2.imshow("windowFrame",frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    video.realease()
    cv2.destroyAllWindows


#####

while True:
        ret, frame =video.read()
        if process_this_frame:

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
                name ="unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        cv2.imshow("Video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
video.realease()
cv2.destroyAllWindows



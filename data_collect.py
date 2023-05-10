import cv2
import os
import face_recognition
import numpy as np

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0 


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
video = cv2.VideoCapture(0)

obama_image = face_recognition.load_image_file("./Imagenes/President_Barack_Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

known_face_names = ["Barack Obama"]
known_face_encodings = [
    obama_face_encoding
]
known_face_names = [
    "Barack Obama"
]


count_fps = 0;
while True:
    # Grab a single frame of video
    ret, frame = video.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    if (count_fps%30 ==0 ):
        face_locations = face_recognition.face_locations(rgb_frame,model="hog")
        face_encodings = face_recognition.face_encodings(frame,face_locations)
    count_fps+=1

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

  
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video.release()
cv2.destroyAllWindows()
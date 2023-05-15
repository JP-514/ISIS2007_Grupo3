import cv2
import os
import face_recognition
import numpy as np
import notification_Manager  as nm
import datetime
import threading

video = cv2.VideoCapture(0)
#facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0 
sending_list =[]

def register_someone():

    per_to_recog =str(input("你的名字 : ")).upper()

   

    if existe:
        print("Esta persona ya existe")
        per_to_recog = str(input("Nuevo nombre: "))

    else:
        take_foto()

def take_foto():
    face_recognition.load_image_file()

def send_notification(arg1):
    nm.send_msg(arg1)

def del_element_sendinig( i):
    return sending_list.remove(i)
    

#####
video = cv2.VideoCapture(0)

obama_image = face_recognition.load_image_file("./Imagenes/President_Barack_Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

ao = face_recognition.load_image_file("./Imagenes/Antonio Ortiz.PNG")
antonioOrtizfaceEncoding = face_recognition.face_encodings(ao)[0]

Ivan_Perez = face_recognition.load_image_file("./Imagenes/Ivan Perez.PNG")
Ivan_Perez_encoding = face_recognition.face_encodings(Ivan_Perez)[0]


Juan_Marcos = face_recognition.load_image_file("./Imagenes/Juan Marcos.PNG")
Juan_Marcos_encoding = face_recognition.face_encodings(Juan_Marcos)[0]

Maria_Carmen  = face_recognition.load_image_file("./Imagenes/Maria Carmen Gallego.PNG")
Maria_Carmen_encoding = face_recognition.face_encodings(Maria_Carmen)[0]

Maria_Josefa_Iglesias  = face_recognition.load_image_file("./Imagenes/Maria Josefa Iglesias.PNG")
Maria_Josefa_Iglesias_encoding = face_recognition.face_encodings(Maria_Josefa_Iglesias)[0]


known_face_encodings = [
    obama_face_encoding,
    antonioOrtizfaceEncoding,
    Ivan_Perez_encoding,
    Juan_Marcos_encoding,
    Maria_Carmen_encoding,
    Maria_Josefa_Iglesias_encoding
]
known_face_names = [
    "Barack Obama",
    "Antonio Ortiz",
    "Ivan Perez",
    "Juan Marcos",
    "Maria Carmen Gallego",
    "Maria Josefa Iglesias"

]

lock = threading.Lock()

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
            

            if (name not in sending_list):
                arg1= name
                with lock:
                    sending_list.append(name)
                t = threading.Thread(target=send_notification,args=(arg1,))
                t.start()

            

  
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
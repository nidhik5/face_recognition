import cv2
import face_recognition
from simple_facerec import SimpleFacerec

#img = cv2.imread(r"C:\\Users\\Nidhi\\Desktop\\projprac\\face recognition\\Nidhi\\IMG_1291.jpg")
#rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img_encoding = face_recognition.face_encodings(rgb_img)[0]

#img2 = cv2.imread(r"C:\\Users\\Nidhi\\Desktop\\projprac\\face recognition\\Nidhi\\IMG_1103.jpg")
#rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#result = face_recognition.compare_faces([img_encoding], img_encoding2)
#print("Result: ", result)

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # Check if frame is valid
    if not ret:
        print("Error: failed to capture frame")
        break

    # Resize frame
    if frame.shape[0] > 0 and frame.shape[1] > 0:
        resized_frame = cv2.resize(frame, (800, 600))
    else:
        print("Error: invalid frame dimensions")
        break

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(resized_frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(resized_frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", resized_frame)

    #key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

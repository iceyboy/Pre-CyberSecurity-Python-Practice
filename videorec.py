import cv2

cap = cv2.VideoCapture(r'C:\Users\stezz\OneDrive\Pictures\btimages\test.mp4')

face_cascade = cv2.CascadeClassifier(r'C:\Users\stezz\OneDrive\Pictures\btimages\haarcascade_frontalface_default.xml')

while(True):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 100, 200), 3)



    cv2.imshow('Frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

cap.release()

cv2.destroyAllWindows()

import cv2

face = cv2.CascadeClassifier(r'C:\Users\stezz\OneDrive\Pictures\btimages\haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(r'C:\Users\stezz\OneDrive\Pictures\btimages\haarcascade_eye.xml')
mouth = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
upperbody = cv2.CascadeClassifier(r'C:\Users\stezz\OneDrive\Pictures\btimages\haarcascade_upperbody.xml')

bw = 80
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
wearingfontcolor = (255, 255, 255)
notwearingfontcolor = (0, 0, 255)
thickness = 2
fontscale = 1
wearing = "Mask found"
notwearing = "Face not wearing a mask"

cap = cv2.VideoCapture(r'C:\Users\stezz\OneDrive\Pictures\btimages\facemask1.mp4')

while 1:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, black_and_white) = cv2.threshold(gray, bw, 255, cv2.THRESH_BINARY)

    faces = face.detectMultiScale(gray, 1.1, 4)

    faces_bw = face.detectMultiScale(black_and_white, 1.1, 4)


    if(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, "No face found...", org, font, fontscale, wearingfontcolor, thickness, cv2.LINE_AA)
    elif(len(faces) == 0 and len(faces_bw) == 1):
        cv2.putText(img, wearing, org, font, fontscale, wearingfontcolor, thickness, cv2.LINE_AA)
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 200), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            mouthrects = mouth.detectMultiScale(gray, 1.5, 5)

        if(len(mouthrects) == 0):
            cv2.putText(img, wearing, org, font, fontscale, wearingfontcolor, thickness, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mouthrects:

                if(y < my < y + h):
                    cv2.putText(img, notwearing, org, font, fontscale, notwearingfontcolor, thickness, cv2.LINE_AA)
                    break

    cv2.imshow('Mask Detection', img)
    if cv2.waitKey(25) & 0xFF == ord('x'):
        break



cap.release()
cv2.destroyAllWindows()
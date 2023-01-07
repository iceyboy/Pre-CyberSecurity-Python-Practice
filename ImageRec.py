import cv2
import sys

imagePath = sys.argv[0]
cascPath = (r'C:\Users\stezz\OneDrive\Pictures\btimages\haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(r'C:\Users\stezz\OneDrive\Pictures\btimages\test1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 100, 200), 2)

cv2.imshow("bt", image)
cv2.waitKey(0)
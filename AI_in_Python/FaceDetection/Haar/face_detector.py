import cv2 #pip install opencv-python

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image file
img = cv2.imread('federer.jpg')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(img)
print(face_coordinates) # list of coordinates (x, y, w, h)


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)


#Display
windowName = 'FaceDetector'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
cv2.imshow(windowName, img)
cv2.waitKey() # waits for a key stroke before exiting
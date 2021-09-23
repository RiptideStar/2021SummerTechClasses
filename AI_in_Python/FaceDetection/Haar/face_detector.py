import cv2 #pip install opencv-python

#Display
windowName = 'FaceDetector'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# webcam = cv2.VideoCapture(0)
# while True:
#     readFrame, frame = webcam.read()

#     grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#     for (x, y, w, h) in face_coordinates:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

#     cv2.imshow(windowName, frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# webcam.release()
# cv2.destroyAllWindows()


################# IMG ##############


#choose an image file
img = cv2.imread('rock1.jpeg')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates) # list of coordinates (x, y, w, h)


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 5)


cv2.imshow(windowName, img)
cv2.waitKey() # waits for a key stroke before exiting
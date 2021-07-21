import cv2 #pip install opencv-python

trained_face_data = cv2.CascadeClassifier('haarcascade_frontal_default.xml')

#choose an image file
img = cv2.imread('federer.jpg')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(img)
print(face_coordinates)



# #Display
# windowName = 'FaceDetector'
# cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
# cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
# cv2.imshow(windowName, img)
# cv2.waitKey() # waits for a key stroke before exiting


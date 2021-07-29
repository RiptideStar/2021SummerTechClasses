import cv2

car_classifier_filename = 'cars.xml'

car_detector = cv2.CascadeClassifier(car_classifier_filename)

#Display
windowName = 'CarDetector'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

##################### IMG STUFF #############
img_file = 'cars_highway.jpeg'

img = cv2.imread(img_file)
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_coordinates = car_detector.detectMultiScale(grayscaled_img)

for (x, y, w, h) in car_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)

cv2.imshow(windowName, img)    

cv2.waitKey()
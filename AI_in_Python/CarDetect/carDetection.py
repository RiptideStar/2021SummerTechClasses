import cv2

car_classifier_filename = 'cars.xml'

car_detector = cv2.CascadeClassifier(car_classifier_filename)

#Display
windowName = 'CarDetector'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

##################### IMG STUFF #############
# img_file = 'cars_highway.jpeg'

# img = cv2.imread(img_file)
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# car_coordinates = car_detector.detectMultiScale(grayscaled_img)

# for (x, y, w, h) in car_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)

# cv2.imshow(windowName, img)    

# cv2.waitKey()

#################### Video ############
video_file = "traffic_flow.mp4"

video = cv2.VideoCapture(video_file)

while True:
    readFrame, frame = video.read()

    if readFrame:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars
    cars = car_detector.detectMultiScale(gray_frame)

    # draw cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(20) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()    
import cv2
from mtcnn import MTCNN

detector = MTCNN()

#Display
windowName = 'FaceDetector'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

webcam = cv2.VideoCapture(0)

while True:
    readFrame, frame = webcam.read()

    faces = detector.detect_faces(frame)

    for face in faces:
        (x, y, w, h) = face['box']
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        keypoints = face['keypoints']
        cv2.circle(frame, (keypoints['left_eye']), 2, (128, 0, 0), 2)
        cv2.circle(frame, (keypoints['right_eye']), 2, (128, 0, 0), 2)
        cv2.circle(frame, (keypoints['nose']), 2, (128, 0, 0), 2)
        cv2.circle(frame, (keypoints['mouth_left']), 2, (128, 0, 0), 2)
        cv2.circle(frame, (keypoints['mouth_right']), 2, (128, 0, 0), 2)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
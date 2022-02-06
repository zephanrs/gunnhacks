from time import time

import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    img = cap.read()

    cv2.imshow('Raw', img)
    key = cv.waitKey(1)

    if key == ord('p'):
        cv2.imwrite('positive/{}.jpg'.format(time()), img)
    if key == ord('n'):
        cv2.imwrite('negative/{}.jpg'.format(time()), img)
    if key == ord('k'):
        break
cv2.destroyAllWindows()
print("data collection completed")


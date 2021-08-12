import cv2
import numpy as np

path = '/Users/veersingh/Desktop/1.png'
original_img = cv2.imread(path)
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img = cv2.bitwise_not(img)

# apply dilation
img = cv2.dilate(img, np.ones((30,30)))
img = cv2.bitwise_not(img)

contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST,
                                           cv2.CHAIN_APPROX_SIMPLE)[-2:]

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    xmin = x
    ymin = y
    xmax = x + w
    ymax = y + h
    cv2.rectangle(original_img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 5)

cv2.imshow('sda', original_img)
cv2.waitKey(0)

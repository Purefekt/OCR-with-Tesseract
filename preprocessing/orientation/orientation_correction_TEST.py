import cv2
import numpy as np

input_image = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/orientation/orientation_dataset/601.jpg'
original = cv2.imread(input_image)

img = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (9, 9), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
dilate = cv2.dilate(thresh, kernel, iterations=5)


contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

largestContour = contours[0]
minAreaRect = cv2.minAreaRect(largestContour)
box = cv2.boxPoints(minAreaRect)
box = np.int0(box)
# convert to bgr for drawing contour
dilate_bgr = cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR)
largest_contour_drawn = cv2.drawContours(dilate_bgr, [box], 0, (0, 0, 255), 10)

# angle is the third element of minAreaRect
angle = minAreaRect[2]

# Calculate the skew angle
if angle > 45:
    angle = 90 - angle
else:
    angle = -angle

skew_angle = round((-1.0 * angle), 2)

######################################## Fixing
rows = img.shape[0]
cols = img.shape[1]
img_center = (cols / 2, rows / 2)

M = cv2.getRotationMatrix2D(img_center, skew_angle, 1)
rotated_image = cv2.warpAffine(img, M, (cols, rows), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

cv2.imshow('Original', original)
cv2.imshow('Applied Preprocessing', thresh)
cv2.imshow('Applied Dilation', dilate)
cv2.imshow('Largest Contour', largest_contour_drawn)
cv2.imshow('Corrected', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

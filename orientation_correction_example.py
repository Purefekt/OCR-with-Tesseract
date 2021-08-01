import cv2
from preprocessing.orientation_correction import orientation_correction

image = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/orientation/orientation_dataset/19.jpg'
img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

out = orientation_correction(img).orientation_correction()

cv2.imshow('original', img)
cv2.imshow('corrected', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
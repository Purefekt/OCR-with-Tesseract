import cv2
import numpy as np

img = cv2.imread("/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg")


# grayscale to reduce computation
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal with median blur
def noise_removal(image):
    # (source, order)
    return cv2.medianBlur(image, 5)


# binarization with thresholding, Otsu algorithm
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation to enlarge the smaller texts
def dilation(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion to reduce the larger texts
def erosion(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion and dilation but less destructive
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


gray = grayscale(img)
noise = noise_removal(gray)
thresh = thresholding(noise)
dilation = dilation(thresh)
erosion = erosion(dilation)
opening = opening(erosion)
canny = canny(opening)




#cv2.imshow('Original Image', img)
#cv2.imshow('Gray',gray)
cv2.imshow('noise',noise)
#cv2.imshow('thresh',thresh)
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
#cv2.imshow('opening',gray)
#cv2.imshow('canny', canny)
#cv2.imshow('final',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

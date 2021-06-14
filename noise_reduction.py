import cv2
import numpy as np


class noise_reduction:
    def __init__(self, image_path):
        self.image_path = image_path
        self.input_image = cv2.imread(self.image_path)
        print(self.image_path)

    def grayscale(self):
        """converts the image to grayscale, reduces computation"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        return cv2.imshow('Gray', gray)

    def median_blur(self):
        """noise removal with median blur with order 5, works on grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        medianBlur = cv2.medianBlur(gray, 5)
        return cv2.imshow('Median Blur', medianBlur)

    def thresholding(self):
        """binarization with thresholding, Otsu algorithm, works on grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return cv2.imshow('Thresholding', thresh)

    def dilation(self):
        """dilation enlarges smaller, blurred texts"""
        kernel = np.ones((5, 5), np.uint8)
        dilate = cv2.dilate(self.input_image, kernel, iterations=1)
        return cv2.imshow('Dilation', dilate)

    def erosion(self):
        """erosion reduces larger texts"""
        kernel = np.ones((5, 5), np.uint8)
        erode = cv2.erode(self.input_image, kernel, iterations=1)
        return cv2.imshow('Erosion', erode)

    def opening(self):
        """opening performs erosion then dilation and is less destructive"""
        kernel = np.ones((5, 5), np.uint8)
        open = cv2.morphologyEx(self.input_image, cv2.MORPH_OPEN, kernel)
        return cv2.imshow('Opening', open)

    def canny(self):
        """canny edge detection"""
        canny_edge = cv2.Canny(self.input_image, 100, 200)
        return cv2.imshow('Canny Edge', canny_edge)


# input image
img = "/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg"


def run():
    noise_reduction(img).grayscale()
    noise_reduction(img).median_blur()
    noise_reduction(img).thresholding()
    noise_reduction(img).dilation()
    noise_reduction(img).erosion()
    noise_reduction(img).opening()
    noise_reduction(img).canny()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


run()
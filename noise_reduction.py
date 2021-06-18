import cv2
import numpy as np


class noise_reduction:
    def __init__(self, image_path):
        self.image_path = image_path
        self.input_image = cv2.imread(self.image_path)

    def grayscale(self):
        """converts the image to grayscale, reduces computation"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        return cv2.imshow('Gray', gray)

    def thresholding(self):
        """binarization with thresholding. Otsu algorithm, works on grayscale, it automatically chooses the threshold
        value for us """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return cv2.imshow('Thresholding', thresh)

    def clahe(self):
        """Increases contrast between background and the text for easier differentiation and icreases sharpess of
        characters for better character segmentation """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        # create a CLAHE object (Arguments are optional). clipLimit = threshold for contrast limiting, tileGrideSize
        # = gridsize for histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_output = clahe.apply(gray)
        return cv2.imshow('CLAHE', clahe_output)

    def gaussian_blur(self):
        """Uses gaussian kernel for convolution. good at removing gaussian noise from the image, kernel size of 5 is
        used here """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        gaussianBlur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
        return cv2.imshow('Gaussian Blur', gaussianBlur)

    def median_blur(self):
        """noise removal with median blur with order 5, works on grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        medianBlur = cv2.medianBlur(gray, 3)
        return cv2.imshow('Median Blur', medianBlur)

    def bilateral_filtering(self):
        """noise removal while preserving the edges. d = diameter of each pixel neighbourhood. sigmaColor = value of
        sigma in colorspace, sigmaSpace = value of sigma in coordinate space """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        bilateralFiltering = cv2.bilateralFilter(gray, d=15, sigmaColor=75, sigmaSpace=75)
        return cv2.imshow('Bilateral Filtering', bilateralFiltering)

    def image_despeckling(self):
        """To remove granular noise.
        h = filter strength, higher value removes more noise but might remove smaller
        elements like commas
        templateWindowSize = size in pixels that is used to compute weights, must be odd,
        recommended = 7
        searchWindowSize = Size in pixels of the window that is used to compute weighted average for
        given pixel. odd, greater value greater time taken, recommended = 21 """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        imageDespeckling = cv2.fastNlMeansDenoising(gray, h=10, templateWindowSize=7, searchWindowSize=21)
        return cv2.imshow("Image Despeckling", imageDespeckling)

    def opening(self):
        """opening performs erosion then dilation and is less destructive, after grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        # 5x5 kernal of all ones
        kernel = np.ones((5, 5), np.uint8)
        open = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        return cv2.imshow('Opening', open)

    def canny(self):
        """canny edge detection, after grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        canny_edge = cv2.Canny(gray, 100, 200)
        return cv2.imshow('Canny Edge', canny_edge)


# input image
img = "/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg"


def run():
    noise_reduction(img).grayscale()
    noise_reduction(img).thresholding()
    noise_reduction(img).clahe()
    noise_reduction(img).gaussian_blur()
    noise_reduction(img).median_blur()
    noise_reduction(img).bilateral_filtering()
    noise_reduction(img).image_despeckling()
    noise_reduction(img).opening()
    noise_reduction(img).canny()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


run()

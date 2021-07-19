import cv2


class noise_reduction_apply:

    def __init__(self, input_image):
        """input_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)"""
        self.input_image = input_image

    def gaussian_blur(self):
        gaussian_blur = cv2.GaussianBlur(self.input_image, (5, 5), 0)
        return gaussian_blur

    def median_blur(self):
        median_blur = cv2.medianBlur(self.input_image, 3)
        return median_blur

    def thresholding(self):
        thresh = cv2.threshold(self.input_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh

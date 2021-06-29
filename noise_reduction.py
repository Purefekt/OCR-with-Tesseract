import cv2


class noise_reduction:

    def __init__(self, input_image):
        """takes in a opencv image"""
        self.input_image = input_image

    def grayscale(self):
        """turning image into grayscale reduces computation cost"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        return gray

    def thresholding(self):
        """binarization with thresholding. Otsu algorithm, works on grayscale, it automatically chooses the threshold
        value for us """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh

    def clahe(self):
        """Increases contrast between background and the text for easier differentiation and icreases sharpess of
        characters for better character segmentation """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        # create a CLAHE object (Arguments are optional). clipLimit = threshold for contrast limiting, tileGrideSize
        # = gridsize for histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_output = clahe.apply(gray)
        return clahe_output

    def gaussian_blur(self):
        """Uses gaussian kernel for convolution. good at removing gaussian noise from the image, kernel size of 5 is
        used here """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        gaussianBlur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
        return gaussianBlur

    def median_blur(self):
        """noise removal with median blur with order 3, works on grayscale"""
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        medianBlur = cv2.medianBlur(gray, 3)
        return medianBlur

    def bilateral_filtering(self):
        """noise removal while preserving the edges. d = diameter of each pixel neighbourhood. sigmaColor = value of
        sigma in colorspace, sigmaSpace = value of sigma in coordinate space """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        bilateralFiltering = cv2.bilateralFilter(gray,
                                                 d=15,
                                                 sigmaColor=75,
                                                 sigmaSpace=75)
        return bilateralFiltering

    def image_despeckling(self):
        """To remove granular noise.
        h = filter strength, higher value removes more noise but might remove smaller
        elements like commas
        templateWindowSize = size in pixels that is used to compute weights, must be odd,
        recommended = 7
        searchWindowSize = Size in pixels of the window that is used to compute weighted average for
        given pixel. odd, greater value greater time taken, recommended = 21 """
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        imageDespeckling = cv2.fastNlMeansDenoising(gray,
                                                    h=10,
                                                    templateWindowSize=7,
                                                    searchWindowSize=21)
        return imageDespeckling

import cv2


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

    def page_rotation(self):
        """"uses largest contour to predict the angle of rotation of the image. Image needs to be preprocessed for 
        best results """
        # grayscale, gaussian blur and thresholding
        gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        gaussianBlur = cv2.GaussianBlur(gray, (9, 9), 0)
        thresh = cv2.threshold(gaussianBlur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # dilation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=5)

        # Finding all contours
        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        # getting largest contour and it angle to be rotated
        largestContour = contours[0]
        # minAreaRect gives the minimum area rotated rectangle (centre(x,y), (width, height), angle)
        minAreaRect = cv2.minAreaRect(largestContour)

        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[2]
        if angle < -45:
            angle = 90 + angle
            print('check')
        angle_to_rotate = -1.0 * angle
        return angle_to_rotate

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


# input image
img = "/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg"
skew_image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img_skew_65.PNG'


def run():
    noise_reduction(img).grayscale()
    noise_reduction(img).thresholding()
    noise_reduction(img).clahe()
    print(noise_reduction(skew_image).page_rotation())
    noise_reduction(img).gaussian_blur()
    noise_reduction(img).median_blur()
    noise_reduction(img).bilateral_filtering()
    noise_reduction(img).image_despeckling()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


run()

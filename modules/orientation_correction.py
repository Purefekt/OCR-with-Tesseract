import cv2


class OrientationCorrection:
    """
    This class has methods to detect the orientation of a scanned document and then tries to correct for that skew
    by rotating the image.

    Attributes:
        input_image: grayscale numpy array image
    """

    def __init__(self, input_image):
        self.input_image = input_image

    @staticmethod
    def get_skewed_angle(img):
        """
        This method calculated the angle of skew

        Args:
            grayscale numpy array image

        Returns:
            float value of the angle
        """
        blur = cv2.GaussianBlur(img, (9, 9), 0)
        thresh = cv2.threshold(blur, 0, 255,
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=5)

        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST,
                                               cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        largestContour = contours[0]
        minAreaRect = cv2.minAreaRect(largestContour)

        # angle is the third element of minAreaRect
        angle = minAreaRect[2]

        # Calculate the skew angle
        if angle > 45:
            angle = 90 - angle
        else:
            angle = -angle

        skew_angle = round((-1.0 * angle), 2)

        return skew_angle

    def orientation_correction(self):
        """
        This method corrects the skew of the image by rotating it using the angle calculated in the previous method

        Args:
            self

        Returns:
            numpy array image where the skew has been corrected
        """
        img = self.input_image
        rows = img.shape[0]
        cols = img.shape[1]
        img_center = (cols / 2, rows / 2)

        skew_angle = OrientationCorrection.get_skewed_angle(img)

        M = cv2.getRotationMatrix2D(img_center, skew_angle, 1)
        rotated_image = cv2.warpAffine(img,
                                       M, (cols, rows),
                                       borderMode=cv2.BORDER_CONSTANT,
                                       borderValue=(255, 255, 255))

        return rotated_image

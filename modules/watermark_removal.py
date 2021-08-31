import cv2


class WatermarkRemoval:
    """
    This class has a method which is used to remove the watermarks or stains on a scanned image

    Attributes:
        input_image: input image path
    """

    def __init__(self, input_image):
        self.input_image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

    def output(self):
        """
        This method will remove the watermark

        Args:
            self

        Returns:
            numpy array image with watermark or stain removed
        """
        watermark = cv2.medianBlur(self.input_image, 19)
        output = cv2.subtract(watermark, self.input_image)
        output = cv2.bitwise_not(output)

        return output

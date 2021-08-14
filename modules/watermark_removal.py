import cv2


class watermark_removal:

    def __init__(self, input_image):
        self.input_image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

    def output(self):
        watermark = cv2.medianBlur(self.input_image, 19)
        output = cv2.subtract(watermark, self.input_image)
        output = cv2.bitwise_not(output)

        return output

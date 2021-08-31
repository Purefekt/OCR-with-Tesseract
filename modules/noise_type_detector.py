import cv2


class NoiseTypeDetector:
    """
    Implementation of the spike detection algorithm which is used to detect the type of noise in an image

    Attributes:
        input_image: a grayscale numpy array image
    """

    # values calculated using noise_detector_range_values.py script
    lower_gaussian = 96.04917198684099
    upper_gaussian = 326.5743861507359

    lower_impulse = 4039.43981828374
    upper_impulse = 8989.931753143906

    def __init__(self, input_image):
        self.input_image = input_image

    @staticmethod
    def sdt_algorithm(img):
        """
        Get the distance of the particular image

        Args:
            grayscale numpy array image

        Returns:
            Float value of the distance
        """
        histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
        H = []
        for i in range(len(histogram)):
            H.append(histogram[i][0])

        D = []
        for i in range(len(H) - 1):
            D.append(H[i + 1] - H[i])

        NL1 = min(D)
        NL2 = max(D)

        distance = NL2 - NL1
        distance = (distance / (img.shape[0] * img.shape[1])) * 100000
        return distance

    def flag(self):
        """
        This method uses the distance calculated by SDT_algorithm() to flag the image as having gaussian noise or
        impulse noise or none.

        Args:
            self

        Returns:
            Int value for flags for gaussian and impulse noise. If image has gaussian noise then the output will be 1,0
        """
        gaussian_flag = 0
        impulse_flag = 0

        distance = NoiseTypeDetector.sdt_algorithm(self.input_image)

        if NoiseTypeDetector.lower_gaussian <= distance <= NoiseTypeDetector.upper_gaussian:
            gaussian_flag = 1
        elif NoiseTypeDetector.lower_impulse <= distance <= NoiseTypeDetector.upper_impulse:
            impulse_flag = 1
        else:
            pass

        return gaussian_flag, impulse_flag

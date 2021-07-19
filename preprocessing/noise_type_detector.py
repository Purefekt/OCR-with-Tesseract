import cv2


class noise_type_detector:

    # values calculated previously
    lower_gaussian = 96.04917198684099
    upper_gaussian = 326.5743861507359

    lower_impulse = 4039.43981828374
    upper_impulse = 8989.931753143906

    def __init__(self, input_image):
        """input_image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)"""
        self.input_image = input_image

    @staticmethod
    def SDT_algorithm(img):
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
        gaussian_flag = 0
        impulse_flag = 0

        distance = noise_type_detector.SDT_algorithm(self.input_image)

        if noise_type_detector.lower_gaussian <= distance <= noise_type_detector.upper_gaussian:
            gaussian_flag = 1
        elif noise_type_detector.lower_impulse <= distance <= noise_type_detector.upper_impulse:
            impulse_flag = 1
        else:
            pass

        return gaussian_flag, impulse_flag

import cv2
import math
import scipy.signal
import numpy as np
import statistics


class noise_reduction_apply:

    def __init__(self, input_image):
        """input_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)"""
        self.input_image = input_image

    # opencv gaussian blur
    def gaussian_blur(self):
        gaussian_blur = cv2.GaussianBlur(self.input_image, (5, 5), 0)
        return gaussian_blur

    # gaussian noise removal algorithm from paper
    @staticmethod
    def get_gaussian_noise_sd(img):
        M = img.shape[0]
        N = img.shape[1]

        pi_by_2_sqrt = math.sqrt((math.pi / 2))

        MASK = np.array([1, -2, 1, -2, 4, -2, 1, -2, 1]).reshape((3, 3))

        convolved_img_mask = scipy.signal.convolve2d(in1=img,
                                                     in2=MASK,
                                                     mode='same',
                                                     boundary='fill',
                                                     fillvalue=0)

        gaussian_noise_sd = pi_by_2_sqrt * (1 / (6 * M * N)) * (
            abs(convolved_img_mask).sum())

        return gaussian_noise_sd

    def paper_algo_gaussian_removal(self):
        img = self.input_image
        M = img.shape[0]
        N = img.shape[1]

        gaussian_noise_sd = noise_reduction_apply.get_gaussian_noise_sd(
            self.input_image)

        # higher smoothing factor gives better noise removal at the cost of image detail
        smoothing_factor = 5
        W = 3
        threshold = (2 * W) - 1

        no_of_centre_pixels = 0
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                no_of_centre_pixels = no_of_centre_pixels + 1
                image_segment = [
                    img[i - 1][j - 1], img[i - 1][j], img[i - 1][j + 1],
                    img[i][j - 1], img[i][j], img[i][j + 1], img[i + 1][j - 1],
                    img[i + 1][j], img[i + 1][j + 1]
                ]

                centre_pixel = image_segment[4]

                # find absolute difference values, list of 8 elements
                absolute_difference = []
                for k in range(len(image_segment)):
                    # skip the centre pixel
                    if k == 4:
                        continue
                    else:
                        absolute_difference.append(
                            abs(int(image_segment[k]) - int(centre_pixel)))

                pixel_values_except_centre = image_segment[:4] + image_segment[
                    5:]

                DA = []
                count = 0
                for l in range(len(absolute_difference)):
                    if absolute_difference[
                            l] < gaussian_noise_sd * smoothing_factor:
                        DA.append(pixel_values_except_centre[l])
                        count = count + 1
                    else:
                        continue

                if count != 0:
                    mean_of_DA = statistics.mean(DA)
                    if count > threshold:
                        img[i][j] = mean_of_DA
                    else:
                        pass
                else:
                    pass

        return img

    def median_blur(self):
        median_blur = cv2.medianBlur(self.input_image, 3)
        return median_blur

    def thresholding(self):
        thresh = cv2.threshold(self.input_image, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh

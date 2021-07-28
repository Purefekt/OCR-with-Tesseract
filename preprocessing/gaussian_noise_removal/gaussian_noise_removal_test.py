import cv2
import math
import numpy as np
import scipy.signal
import statistics

input_image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/gauss2.jpg'
original_image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
img = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

M = img.shape[0]
N = img.shape[1]


def find_gaussian_noise_sd():
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


gaussian_noise_sd = find_gaussian_noise_sd()
# higher smoothing factor, better noise removal at the cost of image detail
smoothing_factor = 2
W = 3
threshold = (2 * W) - 1

no_of_centre_pixels = 0
for i in range(1, M - 1):
    for j in range(1, N - 1):
        no_of_centre_pixels = no_of_centre_pixels + 1
        image_segment = [
            img[i - 1][j - 1], img[i - 1][j], img[i - 1][j + 1], img[i][j - 1],
            img[i][j], img[i][j + 1], img[i + 1][j - 1], img[i + 1][j],
            img[i + 1][j + 1]
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

        pixel_values_except_centre = image_segment[:4] + image_segment[5:]

        DA = []
        count = 0
        for l in range(len(absolute_difference)):
            if absolute_difference[l] < gaussian_noise_sd * smoothing_factor:
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

print(f'Gaussian noise standard deviation = {gaussian_noise_sd}\n')
print(f'Current Image Segment -> \n{np.array(image_segment).reshape((3, 3))}')
print(f'Centre pixel -> {centre_pixel}\n')
print(f'Absolute difference = {absolute_difference}\n')
print(f'Number of flagged pixels = {count}\n')
print(f'DA = {DA}')
print(f'mean of DA = {mean_of_DA}\n')
print(
    f'New image segment = \n{np.array([img[(M-2) - 1][(N-2) - 1], img[(M-2) - 1][(N-2)], img[(M-2) - 1][(N-2) + 1],img[(M-2)][(N-2) - 1], img[(M-2)][(N-2)], img[(M-2)][(N-2) + 1],img[(M-2) + 1][(N-2) - 1], img[(M-2) + 1][(N-2)], img[(M-2) + 1][(N-2) + 1]]).reshape((3,3))}'
)

gaussian_blur = cv2.GaussianBlur(original_image, (5, 5), 0)

cv2.imshow('Original', original_image)
cv2.imshow('Output', img)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imwrite('check1.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/veersingh/Desktop/noise_detection/gaussian/388016gauimgNoise13.jpg', cv2.IMREAD_GRAYSCALE)

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])


def plot():
    plt.figure('Image')
    plt.imshow(img, cmap='gray')

    plt.figure('Histogram')
    plt.plot(histogram)

    plt.show()


plot()

import cv2
from matplotlib import pyplot as plt


def SDT_algorithm(input_image):
    img = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
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
    return img, histogram, D, distance


input_image = '../../assets/gauss.jpg'
img, histogram, D, distance = SDT_algorithm(input_image=input_image)

print(distance)


def plot():
    plt.figure('Image')
    plt.imshow(img, cmap='gray')

    plt.figure('Histogram')
    plt.plot(histogram)

    plt.figure('D vector')
    plt.plot(D)

    plt.show()


# plot()

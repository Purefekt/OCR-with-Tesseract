import os
import cv2
import numpy as np

"""
Dataset -> https://www.kaggle.com/veersingh230799/images-with-gaussian-or-impulse-noise/settings
This script will go over the training images for gaussian noise (1200 images) and impulse noise (1200 images)
to find the range of values for spike detection algorithm.
It then uses the images in the training set to check how accurate those values are and prints the results.
"""


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


def find_boundary_values(directory):
    distances = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(
                ".jpeg") or filename.endswith(".png"):
            input_image = os.path.join(directory, filename)

            distance = SDT_algorithm(input_image=input_image)[3]
            distances.append(distance)

        else:
            continue

    mean = np.mean(distances)
    standard_dev = np.std(distances)
    lower = mean - 2 * standard_dev
    upper = mean + 2 * standard_dev

    return lower, upper


def test_accuracy(test_directory, train_directory):
    # get the lower and upper values
    lower, upper = find_boundary_values(train_directory)
    total_images = 0
    flagged_images = 0

    for filename in os.listdir(test_directory):
        if filename.endswith(".jpg") or filename.endswith(
                ".jpeg") or filename.endswith(".png"):
            total_images = total_images + 1
            input_image = os.path.join(test_directory, filename)

            distance = SDT_algorithm(input_image=input_image)[3]

            # check if this value is inside the range
            if distance >= lower and distance <= upper:
                flagged_images = flagged_images + 1
            else:
                continue

    return flagged_images, total_images, lower, upper


####################################################################################################################

# Download the dataset from the link and get the paths to the following directories
train_gaussian = ''  # path to dataset/train/gaussian
train_impulse = ''  # path to dataset/train/impulse
test_gaussian = ''  # path to dataset/test/gaussian
test_impulse = ''  # # path to dataset/test/impulse

flagged_images, total_images, lower, upper = test_accuracy(
    test_directory=test_gaussian, train_directory=train_gaussian)
print(f'-----Gaussian Noise-----\n'
      f'lower bound = {lower}\n'
      f'upper bound = {upper}\n'
      f'Total test images = {total_images}\n'
      f'Total flagged images = {flagged_images}\n'
      f'Accuracy = {(flagged_images / total_images) * 100}%\n')

flagged_images, total_images, lower, upper = test_accuracy(
    test_directory=test_impulse, train_directory=train_impulse)
print(f'-----Impulse Noise-----\n'
      f'lower bound = {lower}\n'
      f'upper bound = {upper}\n'
      f'Total test images = {total_images}\n'
      f'Total flagged images = {flagged_images}\n'
      f'Accuracy = {(flagged_images / total_images) * 100}%\n')

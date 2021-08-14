import cv2
import random
import json
import os
import shutil
import numpy as np


def create_random_skew_dataset(input_image_path, dataset_size, a1, a2):
    """to create a dataset in a certain range of angles with random angle values"""
    input_image = cv2.imread(input_image_path)

    # Create dataset directory, NOTE: It deletes the folder if it exists already
    dataset_directory = 'orientation_dataset/'
    if os.path.exists(dataset_directory):
        shutil.rmtree(dataset_directory)
    os.makedirs(dataset_directory)

    angle_values_dict = {}

    rows = input_image.shape[0]
    cols = input_image.shape[1]
    input_image_center = (cols / 2, rows / 2)

    for i in range(dataset_size):
        # get random angle between a1 and a2 upto 2 decimals
        angle = round(random.uniform(a1, a2), 2)
        M = cv2.getRotationMatrix2D(input_image_center, -angle, 1)
        # rotate image at the angle and set background to white
        rotated_image = cv2.warpAffine(input_image,
                                       M, (cols, rows),
                                       borderMode=cv2.BORDER_CONSTANT,
                                       borderValue=(255, 255, 255))
        # add text to the image
        rotated_image = cv2.putText(img=rotated_image,
                                    text='rotated angle = ' + str(angle),
                                    org=(25, 25),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0),
                                    thickness=2)

        # create output images
        file_name = str(i + 1) + '.jpg'
        print(file_name)
        file_path = 'orientation_dataset/' + file_name
        cv2.imwrite(file_path, rotated_image)

        # write to dictinary
        angle_values_dict.update({file_name: angle})

    # writing json output
    json_output = json.dumps(angle_values_dict, indent=4)
    output_json_file = dataset_directory + 'angle_values.json'
    jsonFile = open(output_json_file, "w")
    jsonFile.write(json_output)
    jsonFile.close()


def create_skew_dataset(input_image_path, a1, a2):
    """to create a dataset starting at angle a1 and going to angle a2 with 0.1 degree increments"""
    input_image = cv2.imread(input_image_path)

    # Create dataset directory, NOTE: It deletes the folder if it exists already
    dataset_directory = 'orientation_dataset/'
    if os.path.exists(dataset_directory):
        shutil.rmtree(dataset_directory)
    os.makedirs(dataset_directory)

    angle_values_dict = {}

    rows = input_image.shape[0]
    cols = input_image.shape[1]
    input_image_center = (cols / 2, rows / 2)

    count = 0
    for i in np.arange(a1, a2, 0.1):
        angle = round(i, 2)

        M = cv2.getRotationMatrix2D(input_image_center, -angle, 1)
        # rotate image at the angle and set background to white
        rotated_image = cv2.warpAffine(input_image,
                                       M, (cols, rows),
                                       borderMode=cv2.BORDER_CONSTANT,
                                       borderValue=(255, 255, 255))
        # add text to the image
        rotated_image = cv2.putText(img=rotated_image,
                                    text='rotated angle = ' + str(angle),
                                    org=(25, 25),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0),
                                    thickness=2)

        # create output images
        file_name = str(count + 1) + '.jpg'
        file_path = 'orientation_dataset/' + file_name
        cv2.imwrite(file_path, rotated_image)

        # write to dictinary
        angle_values_dict.update({file_name: angle})

        # print every 100 images to see progress
        if count % 100 == 0:
            print(file_name)

        count = count + 1

    # writing json output
    json_output = json.dumps(angle_values_dict, indent=4)
    output_json_file = dataset_directory + 'angle_values.json'
    jsonFile = open(output_json_file, "w")
    jsonFile.write(json_output)
    jsonFile.close()


# Run
# input_image_path = '/Users/veersingh/Desktop/Internship/data-extraction/assets/orientation_dataset_source_1.jpg'
input_image_path = '/Users/veersingh/Desktop/Internship/data-extraction/assets/orientation_dataset_source_2.png'
dataset_size = 5
a1 = -20
a2 = +20

create_random_skew_dataset(input_image_path, dataset_size, a1, a2)
# create_skew_dataset(input_image_path, a1, a2)

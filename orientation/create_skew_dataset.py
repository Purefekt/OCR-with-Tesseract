import cv2
import random
import json


def create_skew_dataset(input_image_path, dataset_size, output_dir):
    """Creates a dataset of images rotated at small angles between -20 and 20 degrees and creates a json document with
    the filenames and their actual angle values

    Args:
        input_image_path: absolute path of the image we want to create the dataset with
        dataset_size: number of images in this dataset
        output_dir: directory where the images and json file will be saved

    Returns:
        An image for each angle with the angle printed on the top left of the new image along with a dict of the
        filename and its angle of rotation. For example:
        {"0.jpg": 0,
        "1.jpg": 4.72,
        "2.jpg": -10.51}
    """
    input_image = cv2.imread(input_image_path)

    angle_values_dict = {'0.jpg': 0}

    rows = input_image.shape[0]
    cols = input_image.shape[1]
    input_image_center = (cols / 2, rows / 2)

    for i in range(dataset_size):
        # get random angle between -20 and 20 upto 2 decimals
        angle = round(random.uniform(-20, 20), 2)
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
        file_path = output_dir + file_name
        cv2.imwrite(file_path, rotated_image)

        # write to dictinary
        angle_values_dict.update({file_name: angle})

    # writing json output
    json_output = json.dumps(angle_values_dict, indent=4)
    output_json_file = output_dir + 'angle_values.json'
    jsonFile = open(output_json_file, "w")
    jsonFile.write(json_output)
    jsonFile.close()


# Run
input_image_path = '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/0.jpg'
dataset_size = 35
output_dir = '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/'

create_skew_dataset(input_image_path, dataset_size, output_dir)

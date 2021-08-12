from preprocessing.signature_removal import signature_removal
import cv2
import numpy as np
import os
import json

def get_bboxes(image_path):

    # Use signature detection algorithm
    signature = signature_removal(
        cv2.imread(image_path,
                   cv2.IMREAD_GRAYSCALE)).detect_signature()

    # Apply dilation
    signature = cv2.bitwise_not(signature)
    signature = cv2.dilate(signature, np.ones((30, 30)))
    signature = cv2.bitwise_not(signature)

    # Find contours
    contours, hierarchy = cv2.findContours(signature, cv2.RETR_LIST,
                                           cv2.CHAIN_APPROX_SIMPLE)[-2:]
    area = list()
    x_list = list()
    y_list = list()
    w_list = list()
    h_list = list()

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area.append(w * h)
        x_list.append(x)
        y_list.append(y)
        w_list.append(w)
        h_list.append(h)

        # Assuming the largest bbox is the signature
        # largest bbox will be the entire image, so largest true bbox will be the 2nd largest
        sorted_area = area.copy()
        sorted_area.sort()
        # Handle exception for when no signature is detected
        try:
            largest_bbox = sorted_area[-2]
        except:
            largest_bbox = sorted_area[-1]

        # get index of largest true bbox
        largest_bbox_index = area.index(largest_bbox)

        xmin = x_list[largest_bbox_index]
        ymin = y_list[largest_bbox_index]
        w = w_list[largest_bbox_index]
        h = h_list[largest_bbox_index]

        xmax = xmin + w
        ymax = ymin + h

    return xmin, ymin, xmax, ymax

scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images'
json_file_output_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)'

calculated_values = dict()

for filename in os.listdir(scanned_page_images_dir):
    current_image_name = filename
    current_image_path = scanned_page_images_dir + '/' + filename
    print(filename)

    # get bboxes
    xmin, ymin, xmax, ymax = get_bboxes(current_image_path)

    calculated_values[current_image_name] = [xmin, ymin, xmax, ymax]

# writing json output
json_output = json.dumps(calculated_values, indent=4)
output_json_file = json_file_output_dir + '/' + 'calculated_bbox_attempt_2.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()
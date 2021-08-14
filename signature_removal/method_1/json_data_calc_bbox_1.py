import cv2
from modules.signature_removal import signature_removal
import os
import json

images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images'
json_file_output_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)'

calculated_values = dict()
for filename in os.listdir(images_dir):
    current_image_name = filename
    current_image_path = images_dir + '/' + filename
    current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
    print(filename)

    # get bboxes
    xmin, ymin, xmax, ymax = signature_removal(
        current_image).get_signature_bbox()

    calculated_values[current_image_name] = [xmin, ymin, xmax, ymax]

    print(filename, xmin, ymin, xmax, ymax)

# writing json output
json_output = json.dumps(calculated_values, indent=4)
output_json_file = json_file_output_dir + '/' + 'calculated_bbox_1.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()

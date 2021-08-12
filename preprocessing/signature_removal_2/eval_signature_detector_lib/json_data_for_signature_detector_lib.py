import os
import json
import cv2
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.loader import Loader
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.extractor import Extractor
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.cropper import Cropper

scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images'
json_file_output_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)'

signature_detector_values = dict()

for filename in os.listdir(scanned_page_images_dir):
    current_image_name = filename
    current_image_path = scanned_page_images_dir + '/' + filename
    print(filename)

    # Use signature-detector library to find bbox
    image = cv2.imread(current_image_path)
    loader = Loader()
    mask = loader.get_masks(current_image_path)[0]
    extractor = Extractor(amplfier=15)
    labeled_mask = extractor.extract(mask)
    cropper = Cropper()
    try:
        bbox_coords = cropper.run(labeled_mask)
    except:
        bbox_coords = (0, 0, 0, 0)

    xmin, ymin, xmax, ymax = bbox_coords
    # Convert from numpy int64 to integer for JSON serialization
    xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

    signature_detector_values[current_image_name] = [xmin, ymin, xmax, ymax]

# writing json output
json_output = json.dumps(signature_detector_values, indent=4)
output_json_file = json_file_output_dir + '/' + 'signature_detector_values.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()

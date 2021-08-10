import cv2
import json
"""
This script draws the bounding boxes using the ground truth values from the ground truth json file for sanity check.
"""

ground_truth_json_file = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_bbox.json'
scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images'
scanned_page_images_with_ground_truth_bbox_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images_with_ground_truth_bbox'

f = open(ground_truth_json_file,)
ground_truth_bbox = json.load(f)
f.close()

for filename in ground_truth_bbox.keys():
    current_image_name = filename

    xmin = ground_truth_bbox[filename][0]
    ymin = ground_truth_bbox[filename][1]
    xmax = ground_truth_bbox[filename][2]
    ymax = ground_truth_bbox[filename][3]

    # draw bbox with ground truth values
    image = scanned_page_images_dir + '/' + current_image_name
    image = cv2.imread(image)
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 5)
    cv2.imwrite(
        scanned_page_images_with_ground_truth_bbox_dir + '/' +
        current_image_name, image)

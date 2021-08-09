import cv2
import json

"""
This script draws the bounding boxes using the calculated values from the calculated json file.
"""

calculated_json_file = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/calculated_bbox.json'
scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/'
scanned_page_images_with_calc_bbox_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(' \
                                         'tobacco800)/scanned_page_images_with_calc_bbox/ '

f = open(calculated_json_file, )
ground_truth_bbox = json.load(f)
f.close()

for filename in ground_truth_bbox.keys():
    current_image_name = filename

    xmin = ground_truth_bbox[filename][0]
    ymin = ground_truth_bbox[filename][1]
    xmax = ground_truth_bbox[filename][2]
    ymax = ground_truth_bbox[filename][3]

    # draw bbox with ground truth values
    image = scanned_page_images_dir + current_image_name
    image = cv2.imread(image)
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 5)
    cv2.imwrite(scanned_page_images_with_calc_bbox_dir + current_image_name, image)

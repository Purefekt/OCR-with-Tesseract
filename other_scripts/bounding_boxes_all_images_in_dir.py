import pytesseract
from pytesseract import Output
import cv2
import os
import json
"""NOTE: PAGE NUMBER IS WRONG"""

dir_path = '/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf2image_out'
output_dict = {
    "bbox": {
        "x1": None,
        "y1": None,
        "x2": None,
        "y2": None
    },
    "text": None,
    "page": None
}
output_list = []

for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
        # get the path of the jpg file
        image_path = dir_path + '/' + filename
        img = cv2.imread(image_path)
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        no_of_boxes = (len(d['left']))

        for i in range(no_of_boxes):
            # to get rid of empty boxes
            if len(d['text'][i]) != 0:
                text = d['text'][i]
                page_num = d['page_num'][i]
                x1 = d['left'][i]
                y1 = d['top'][i]
                x2 = d['left'][i] + d['width'][i]
                y2 = d['top'][i] + d['height'][i]

                output_dict = {
                    "bbox": {
                        "x1": None,
                        "y1": None,
                        "x2": None,
                        "y2": None
                    },
                    "text": None,
                    "page": None
                }

                output_dict["bbox"]["x1"] = x1
                output_dict["bbox"]["y1"] = y1
                output_dict["bbox"]["x2"] = x2
                output_dict["bbox"]["y2"] = y2
                output_dict["text"] = text
                output_dict["page"] = page_num

                output_list.append(output_dict)

json_output = json.dumps(output_list, indent=4)
print(json_output)

import os
import json
from signature_detect.loader import Loader
from signature_detect.extractor import Extractor
from signature_detect.boundingBox import Bounding_box

images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images'
json_file_output_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)'

calculated_values = dict()
for filename in os.listdir(images_dir):
    current_image_name = filename
    current_image_path = images_dir + '/' + filename
    print(filename)

    # Use signature-detector library to find bbox
    loader = Loader()
    mask = loader.get_masks(current_image_path)[0]
    extractor = Extractor(amplfier=15)
    labeled_mask = extractor.extract(mask)
    try:
        xmin, ymin, w, h = Bounding_box().run(labeled_mask)
        xmax = xmin + w
        ymax = ymin + h
    # handle exception for when no bbox is found
    except:
        xmin, ymin, xmax, ymax = 0, 0, 0, 0

    # Convert from numpy int64 to integer for JSON serialization
    xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

    calculated_values[current_image_name] = [xmin, ymin, xmax, ymax]

# writing json output
json_output = json.dumps(calculated_values, indent=4)
output_json_file = json_file_output_dir + '/' + 'calculated_bbox_2.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()

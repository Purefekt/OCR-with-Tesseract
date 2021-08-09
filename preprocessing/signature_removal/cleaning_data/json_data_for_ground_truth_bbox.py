import xml.etree.ElementTree as ET
import os
import json

"""
This script saves the ground truth bbox values in this json format for each image.
{
    filename1.tif:[
        xmin,
        ymin,
        xmax,
        ymax
    ]
}
"""

ground_truth_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_xml/'
scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/'
json_file_output_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/'

ground_truth_values = dict()

for filename in os.listdir(ground_truth_dir):

    current_xml_file = filename
    current_image_file = filename.replace('.xml', '.tif')

    # Get data from xml ground truth files
    tree = ET.parse(ground_truth_dir + filename)
    root = tree.getroot()
    xmin = int(root[0][0][0].attrib['col'])
    ymin = int(root[0][0][0].attrib['row'])
    w = int(root[0][0][0].attrib['width'])
    h = int(root[0][0][0].attrib['height'])

    xmax = xmin + w
    ymax = ymin + h

    ground_truth_values[current_image_file] = [xmin, ymin, xmax, ymax]

# writing json output
json_output = json.dumps(ground_truth_values, indent=4)
output_json_file = json_file_output_dir + 'ground_truth_bbox.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()

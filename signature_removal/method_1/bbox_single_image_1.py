import cv2
from modules.signature_removal import signature_removal

image_path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images/hxv75f00_1.tif'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
xmin, ymin, xmax, ymax = signature_removal(image).get_signature_bbox()

print(f'xmin -> {xmin}\n'
      f'ymin -> {ymin}\n'
      f'xmax -> {xmax}\n'
      f'ymax -> {ymax}')

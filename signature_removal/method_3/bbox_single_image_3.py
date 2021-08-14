import cv2
from signature_detect.loader import Loader
from signature_detect.extractor import Extractor
from signature_detect.boundingBox import Bounding_box
from modules.signature_removal import signature_removal

# First calculate bbox using method 2, if all coordinates are 0 then use method 1

image_path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images/hxv75f00_1.tif'

# use method 2
loader = Loader()
mask = loader.get_masks(image_path)[0]
extractor = Extractor(amplfier=15)
labeled_mask = extractor.extract(mask)
try:
    xmin, ymin, w, h = Bounding_box().run(labeled_mask)
    xmax = xmin + w
    ymax = ymin + h
# handle exception for when no bbox is found
except:
    xmin, ymin, xmax, ymax = 0, 0, 0, 0

# use method 1
if (xmin and ymin and xmax and ymax) == 0:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    xmin, ymin, xmax, ymax = signature_removal(image).get_signature_bbox()

# Convert from numpy int64 to integer for JSON serialization
xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)

print(f'xmin -> {xmin}\n'
      f'ymin -> {ymin}\n'
      f'xmax -> {xmax}\n'
      f'ymax -> {ymax}')
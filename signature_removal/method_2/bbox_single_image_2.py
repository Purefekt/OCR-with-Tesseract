from signature_detect.loader import Loader
from signature_detect.extractor import Extractor
from signature_detect.boundingBox import Bounding_box

path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images/ygs60f00-page02_2.tif'

loader = Loader()
mask = loader.get_masks(path)[0]
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

print(f'xmin -> {xmin}\n'
      f'ymin -> {ymin}\n'
      f'xmax -> {xmax}\n'
      f'ymax -> {ymax}')

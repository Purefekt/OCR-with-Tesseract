import cv2
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.loader import Loader
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.extractor import Extractor
from preprocessing.signature_removal_2.getting_bbox_coords_with_library.cropper import Cropper

# Need to install ImageMagick, for macOS
# brew install imagemagick

test_image_path = '/Users/veersingh/Desktop/Internship/data-extraction/assets/signature1.tif'
image = cv2.imread(test_image_path)
loader = Loader()
mask = loader.get_masks(test_image_path)[0]
extractor = Extractor(amplfier=15)
labeled_mask = extractor.extract(mask)
cropper = Cropper()
xmin, ymin, xmax, ymax = cropper.run(labeled_mask)
print(xmin, ymin, xmax, ymax)

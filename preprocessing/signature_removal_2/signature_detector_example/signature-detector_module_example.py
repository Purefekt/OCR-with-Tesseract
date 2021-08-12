import cv2
import matplotlib.pyplot as plt
from signature_detect.loader import Loader
from signature_detect.extractor import Extractor
from signature_detect.cropper import Cropper


def show_image(img):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(img)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()


path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/mtq30d00_4.tif'
image = cv2.imread(path)

# Loader
loader = Loader()
mask = loader.get_masks(path)[0]

# Extractor
extractor = Extractor(amplfier=15)
labeled_mask = extractor.extract(mask)

# Cropper
cropper = Cropper()
results = cropper.run(labeled_mask)

signature = results[0]["cropped_mask"]
show_image(signature)

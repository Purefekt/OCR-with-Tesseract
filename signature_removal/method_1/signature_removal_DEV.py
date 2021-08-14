import cv2
from skimage import measure
from skimage.color import label2rgb
from skimage.measure import regionprops
from skimage import morphology
import numpy as np

image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/signature1.tif'

img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
# Set the pixel values to either 0(black) or 255(white)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

# Connected component analysis by scikit-learn framework
# Set all white pixels to True(1) and all black pixels to False(0)
blobs = img > 254
# skimage.measure.label() will label the connected pixels where the background is white.
# Basically it will only affect the black pixels of our thresholded image, white pixels are labelled as 0.
blobs_labels = measure.label(
    blobs,
    background=1,
)
# skimage.color.label2rgb() will use the pixels labelled in the prev step and give them different colours for
# better visualization.
# bg_label=0 indicates that any pixel with value 0 will be treated as background and will not be coloured.
image_label_overlay = label2rgb(blobs_labels, bg_label=0)
cv2.imshow('Connected Regions in Various Colours', image_label_overlay)

# Now we have different connected regions labelled, but we need to preserve the text and only detect/remove the
# signature which will always be bigger than most text

# skimage.measure.regionprops takes in the labelled image and gives a list of several properties of the
# labelled regions (ignores values with 0) like area of the labelled region.
total_connected_regions = len(regionprops(blobs_labels))
print(f'Number of total connected regions --> {total_connected_regions}')

# Now we need to remove small outlier regions and large outlier regions. We have some experiment based constants which
# we will use alongside the average region area to identify them. These are for A4 size scans.

# These parameters are used to remove small size outlier connected pixel regions
small_parameter_1 = 84
small_parameter_2 = 250
small_parameter_3 = 100
# These parameters are used to remove large size outlier connected pixel regions
large_parameter_1 = 18

total_area = 0
count = 0
for region in regionprops(blobs_labels):
    # To remove really small regions
    if region.area > 10:
        total_area = total_area + region.area
        count = count + 1
average = (total_area / count)

a4_small_size_threshold = (
    (average / small_parameter_1) * small_parameter_2) + small_parameter_3
a4_large_size_threshold = a4_small_size_threshold * large_parameter_1

# We will take the connected regions and remove the outliers by removed regions with area less than the
# small size outlier and larger than the large size outlier

# Removes small outliers
signature = morphology.remove_small_objects(blobs_labels,
                                            a4_small_size_threshold)

# Removes large outliers
component_sizes = np.bincount(signature.ravel())
too_large = component_sizes > a4_large_size_threshold
too_large_mask = too_large[signature]
# Sets all large outliers to 0
signature[too_large_mask] = 0

connected_regions_in_given_range = len(regionprops(signature))
print(
    f'Number of connected regions in the given range--> {connected_regions_in_given_range}'
)

# convert from int32 to unint8 for opencv
signature = np.uint8(signature)
signature = cv2.threshold(signature, 0, 255,
                          cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# Getting image without signature
img_wo_signature = cv2.subtract(signature, img)
img_wo_signature = cv2.bitwise_not(img_wo_signature)

cv2.imshow('Signature', signature)
cv2.imshow('Image without Signature', img_wo_signature)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

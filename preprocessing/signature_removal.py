import cv2
from skimage import measure
from skimage.measure import regionprops
from skimage import morphology
import numpy as np


class signature_removal:
    """
    input = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    output = numpy.ndarray
    """

    def __init__(self, input_image):
        self.input_image = input_image

    @staticmethod
    def process(img):
        # Binarize
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

        # Connected component analysis by scikit-learn framework
        blobs = img > 254
        blobs_labels = measure.label(
            blobs,
            background=1,
        )

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

        a4_small_size_threshold = ((average / small_parameter_1) *
                                   small_parameter_2) + small_parameter_3
        a4_large_size_threshold = a4_small_size_threshold * large_parameter_1

        # Removes small outliers
        signature = morphology.remove_small_objects(blobs_labels,
                                                    a4_small_size_threshold)

        # Removes large outliers
        component_sizes = np.bincount(signature.ravel())
        too_large = component_sizes > a4_large_size_threshold
        too_large_mask = too_large[signature]
        # Sets all large outliers to 0
        signature[too_large_mask] = 0

        # Getting the signature
        signature = np.uint8(signature)
        signature = cv2.threshold(signature, 0, 255,
                                  cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        """Getting image without signature"""
        img_wo_signature = cv2.subtract(signature, img)
        img_wo_signature = cv2.bitwise_not(img_wo_signature)

        return signature, img_wo_signature

    def detect_signature(self):
        signature = signature_removal.process(self.input_image)[0]
        return signature

    def get_image_without_signature(self):
        img_wo_signature = signature_removal.process(self.input_image)[1]
        return img_wo_signature

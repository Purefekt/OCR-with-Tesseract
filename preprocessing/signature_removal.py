import cv2
from skimage import measure
from skimage.color import label2rgb
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
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        """Blob Detection"""
        blobs = img > img.mean()
        blobs_labels = measure.label(
            blobs,
            background=1,
        )
        image_label_overlay = label2rgb(blobs_labels, image=img, bg_label=0)

        the_biggest_component = 0
        total_area = 0
        counter = 0
        average = 0.0
        for region in regionprops(blobs_labels):
            if region.area > 10:
                total_area = total_area + region.area
                counter = counter + 1
            if region.area >= 250:
                if region.area > the_biggest_component:
                    the_biggest_component = region.area

        # Threshold, if the value is greater than this then it is identified as a signature
        average = (total_area / counter)
        # constant for A4 size paper, works best with A4
        a4_constant = ((average / 84.0) * 250.0) + 100
        """Getting the signature"""
        signature = morphology.remove_small_objects(blobs_labels, a4_constant)
        # convert from int32 to unint8 for opencv
        signature = np.uint8(signature)
        signature = cv2.threshold(signature, 0, 255,
                                  cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        """Getting image without signature"""
        img_wo_signature = cv2.subtract(signature, img)
        img_wo_signature = cv2.bitwise_not(img_wo_signature)

        return signature, img_wo_signature

    def get_signature(self):
        signature = signature_removal.process(self.input_image)[0]
        return signature

    def get_image_without_signature(self):
        img_wo_signature = signature_removal.process(self.input_image)[1]
        return img_wo_signature

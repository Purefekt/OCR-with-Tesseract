import cv2
from skimage import measure
from skimage.measure import regionprops
from skimage import morphology
import numpy as np


class signature_removal:
    """
    Class Methods:
    process: applies signature detection on the input image. returns image with just the signature and image without
    the signature.

    get_image_without_signature: returns image with the signature removed.

    get_signature_bbox: returns the top left edge and bottom right edge of bounding boxes around the detected
    signature.

    get_detected_signature: returns image with just the signature cropped.
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

    def get_image_without_signature(self):
        img_wo_signature = signature_removal.process(self.input_image)[1]
        return img_wo_signature

    def get_signature_bbox(self):
        """
        :return: xmin, ymin, xmax, ymax
        (xmin, ymin) -> top left edge of bbox
        (xmax, ymax) -> bottom right edge of bbox
        """
        # Isolate the signature
        signature = signature_removal.process(self.input_image)[0]

        # Apply dilation
        signature = cv2.bitwise_not(signature)
        signature = cv2.dilate(signature, np.ones((30, 30)))
        signature = cv2.bitwise_not(signature)

        # Find contours
        contours, hierarchy = cv2.findContours(signature, cv2.RETR_LIST,
                                               cv2.CHAIN_APPROX_SIMPLE)[-2:]
        area = list()
        x_list = list()
        y_list = list()
        w_list = list()
        h_list = list()

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            area.append(w * h)
            x_list.append(x)
            y_list.append(y)
            w_list.append(w)
            h_list.append(h)

            # Assuming the largest bbox is the signature
            # largest bbox will be the entire image, so largest true bbox will be the 2nd largest
            sorted_area = area.copy()
            sorted_area.sort()
            # Handle exception for when no signature is detected
            try:
                largest_bbox = sorted_area[-2]
            except:
                largest_bbox = sorted_area[-1]

            # get index of largest true bbox
            largest_bbox_index = area.index(largest_bbox)

            xmin = x_list[largest_bbox_index]
            ymin = y_list[largest_bbox_index]
            w = w_list[largest_bbox_index]
            h = h_list[largest_bbox_index]

            xmax = xmin + w
            ymax = ymin + h

        return xmin, ymin, xmax, ymax

    def get_detected_signature(self):
        """
        :return: cropped signature as a numpy array
        """
        xmin, ymin, xmax, ymax = signature_removal(
            self.input_image).get_signature_bbox()
        crop_img = self.input_image[ymin:ymax, xmin:xmax]

        return crop_img

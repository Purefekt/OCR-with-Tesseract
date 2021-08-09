import cv2
from preprocessing.signature_removal import signature_removal


def get_bbox_calculated(image):
    signature = signature_removal(cv2.imread(image, cv2.IMREAD_GRAYSCALE)).detect_signature()

    contours, hierarchy = cv2.findContours(signature, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
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

    # largest bbox will be the entire image, so largest true bbox will be the 2nd largest
    sorted_area = area.copy()
    sorted_area.sort()
    largest_bbox = sorted_area[-2]

    # get index of largest true bbox
    largest_bbox_index = area.index(largest_bbox)

    xmin = x_list[largest_bbox_index]
    ymin = y_list[largest_bbox_index]
    w = w_list[largest_bbox_index]
    h = h_list[largest_bbox_index]

    xmax = xmin + w
    ymax = ymin + h

    return xmin, ymin, xmax, ymax


image = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/aao54e00_2.tif'
original_image = cv2.imread(image)

# Ground truth values for this particular image
xmin_gt = 1514
ymin_gt = 708
w = 627
h = 206
xmax_gt = xmin_gt + w
ymax_gt = ymin_gt + h

# Calculated values for this particular image
xmin_c, ymin_c, xmax_c, ymax_c = get_bbox_calculated(image)

# draw bbox for ground truth values in red color
original_image = cv2.rectangle(original_image, (xmin_gt, ymin_gt), (xmax_gt, ymax_gt), (0, 0, 255), 5)
# draw bbox for calculated values in blue color
original_image = cv2.rectangle(original_image, (xmin_c, ymin_c), (xmax_c, ymax_c), (255, 0, 0), 5)

print(f'%%%%% Ground Truh Values %%%%%\n'
      f'xmin = {xmin_gt}\n'
      f'ymin = {ymin_gt}\n'
      f'xmax = {xmax_gt}\n'
      f'ymax = {ymax_gt}')

print(f'%%%%% Calculated Values %%%%%\n'
      f'xmin = {xmin_c}\n'
      f'ymin = {ymin_c}\n'
      f'xmax = {xmax_c}\n'
      f'ymax = {ymax_c}')

cv2.imshow('calculated', original_image)
cv2.waitKey(0)

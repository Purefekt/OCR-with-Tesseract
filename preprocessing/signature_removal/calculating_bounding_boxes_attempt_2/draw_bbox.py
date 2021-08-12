import cv2

image_path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/aao54e00_2.tif'

xmin = 1498
ymin = 718
xmax = 2152
ymax = 921

image = cv2.imread(image_path)
cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 5)
cv2.imshow('sda', image)
cv2.waitKey(0)

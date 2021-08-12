import cv2

image_path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/mtq30d00_4.tif'

xmin = 1463
ymin = 182
xmax = 1601
ymax = 290

image = cv2.imread(image_path)
cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 5)
cv2.imshow('sda', image)
cv2.waitKey(0)

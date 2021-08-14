import cv2

image_path = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/images/gmk15f00.tif'

xmin = 135
ymin = 395
xmax = 1108
ymax = 405

image = cv2.imread(image_path)
cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 5)
# cv2.imwrite('/Users/veersingh/Desktop/old.png', image)
cv2.imwrite('/Users/veersingh/Desktop/new.png', image)

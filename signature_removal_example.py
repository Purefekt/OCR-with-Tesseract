import cv2
from modules.signature_removal import signature_removal

image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/signature3.tif'
original = cv2.imread(image)

img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

signature = signature_removal(input_image=img).get_detected_signature()
image_without_sign = signature_removal(
    input_image=img).get_image_without_signature()

cv2.imshow('Original', original)
cv2.imshow('Signature', signature)
cv2.imshow('Image without Signature', image_without_sign)
cv2.waitKey(0)
cv2.destroyAllWindows()

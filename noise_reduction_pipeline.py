import cv2
from preprocessing.watermark_removal import watermark_removal
from preprocessing.noise_type_detector import noise_type_detector
from preprocessing.noise_reduction_apply import noise_reduction_apply

#image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/stain1.png'
image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/stain2.jpg'

"""First remove the watermark or stain"""
watermark_removed = watermark_removal(image).output()

"""Second check for gaussian noise or impulse noise"""
gaussian_flag, impulse_flag = noise_type_detector(watermark_removed).flag()

"""Third apply filter depending on the flag"""
if gaussian_flag == 1:
    third = noise_reduction_apply(watermark_removed).gaussian_blur()
    print(gaussian_flag)
elif impulse_flag == 1:
    third = noise_reduction_apply(watermark_removed).median_blur()
    print(impulse_flag)
else:
    third = watermark_removed
    print('0')

"""Fourth apply thresholding"""
output = noise_reduction_apply(third).thresholding()


cv2.imshow('Original', cv2.imread(image))
#cv2.imshow('STEP 0', cv2.imread(image, cv2.IMREAD_GRAYSCALE))
#cv2.imshow('STEP 1', watermark_removed)
#cv2.imshow('STEP 3', third)
cv2.imshow('STEP 4', output)

cv2.waitKey(0)
cv2.destroyAllWindows()

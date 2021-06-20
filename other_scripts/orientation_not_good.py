import cv2
import pytesseract
import re


img = cv2.imread('/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img_skew_315.PNG')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#cv2.imshow('Thresholding', thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#im = cv2.imread(str(imPath), cv2.IMREAD_COLOR)
newdata=pytesseract.image_to_osd(img)
output = re.search('(?<=Rotate: )\d+', newdata).group(0)
#print(output)
print(newdata)
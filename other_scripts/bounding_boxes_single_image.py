import pytesseract
from pytesseract import Output
import cv2


img = cv2.imread('/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf2image_out/Page_1.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
no_of_boxes = (len(d['left']))

for i in range(no_of_boxes):
    if len(d['text'][i]) != 0:
        text = d['text'][i]
        page_num = d['page_num'][i]
        x1 = d['left'][i]
        y1 = d['top'][i]
        x2 = d['left'][i] + d['width'][i]
        y2 = d['top'][i] + d['height'][i]
        print(text)
        print(page_num)
        print(x1)
        print(y1)
        print(x2)
        print(y2)
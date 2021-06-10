import cv2
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
import os
import json
import shutil


class OCR:
    def __init__(self, input_path, language, oem, psm):
        self.input_path = input_path
        self.language = language
        self.oem = oem
        self.psm = psm
        #path to the dir where the pdf is stored
        self.input_pdf_directory = os.path.dirname(os.path.realpath(self.input_path))
        #path of the newly created dir which contains all images
        self.path_of_image_list = self.input_pdf_directory + '/pdf2image_out'

    def pdf_to_images(self):
        pages = convert_from_path(self.input_path, 500)
        # makes the pdf2image_out dir
        #os.makedirs(self.input_pdf_directory + '/pdf2image_out')
        if os.path.exists(self.input_pdf_directory + '/pdf2image_out'):
            shutil.rmtree(self.input_pdf_directory + '/pdf2image_out')
        os.makedirs(self.input_pdf_directory + '/pdf2image_out')

        i = 1
        for page in pages:
            image_name = self.path_of_image_list + '/Page_' + str(i) + '.jpg'
            page.save(image_name, "JPEG")
            i = i + 1

    def ocr_on_images(self):
        output_list = []

        for filename in os.listdir(self.path_of_image_list):
            if filename.endswith(".jpg"):
                # get the path of the jpg file
                image_path = self.path_of_image_list + '/' + filename
                img = cv2.imread(image_path)
                #creating custom config for psm and oem
                custom_oem_psm_config = r'--oem ' + str(self.oem) + r' --psm ' + str(self.psm)
                d = pytesseract.image_to_data(img, self.language, config=custom_oem_psm_config, output_type=Output.DICT)
                no_of_boxes = (len(d['left']))

                for i in range(no_of_boxes):
                    # to get rid of empty boxes
                    if len(d['text'][i]) != 0:
                        text = d['text'][i]
                        page_num = d['page_num'][i]
                        x1 = d['left'][i]
                        y1 = d['top'][i]
                        x2 = d['left'][i] + d['width'][i]
                        y2 = d['top'][i] + d['height'][i]

                        output_dict = {"bbox":
                                           {"x1": None,
                                            "y1": None,
                                            "x2": None,
                                            "y2": None},
                                       "text": None,
                                       "page": None}

                        output_dict["bbox"]["x1"] = x1
                        output_dict["bbox"]["y1"] = y1
                        output_dict["bbox"]["x2"] = x2
                        output_dict["bbox"]["y2"] = y2
                        output_dict["text"] = text
                        output_dict["page"] = page_num

                        output_list.append(output_dict)

        #writing json output
        json_output = json.dumps(output_list, indent=4)
        jsonFile = open(self.input_pdf_directory + "/data.json", "w")
        jsonFile.write(json_output)
        jsonFile.close()

#Parameters
input_path = '/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf_test.pdf'
language = 'eng'
oem = '3'
psm = '3'

def run():
    OCR(input_path,language,oem,psm).pdf_to_images()
    OCR(input_path, language, oem, psm).ocr_on_images()

run()
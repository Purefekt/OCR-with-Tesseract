import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
import os
import json


class ocr:
    """input can be either an image or a pdf"""

    def __init__(self, input_path, language='eng', oem=3, psm=3):
        self.input_path = input_path
        self.language = language
        self.oem = oem
        self.psm = psm

    def basic_ocr(self):
        custom_oem_psm_config = r'--oem ' + str(self.oem) + r' --psm ' + str(
            self.psm)
        output = pytesseract.image_to_string(self.input_path,
                                             lang=self.language,
                                             config=custom_oem_psm_config)
        return output

    def ocr_on_pdf(self):
        """converts the current page into an image, saves it and then runs ocr on that page.
        Once completed moves on to the next image and overwrites the previous image"""

        output_list = []

        pdf_page_images = convert_from_path(self.input_path)

        for i in range(len(pdf_page_images)):

            pdf_page_images[i].save('current_page.jpg', 'JPEG')
            current_page = 'current_page.jpg'
            current_page_num = i + 1

            """applying bounding boxes to current page"""
            # creating custom config for psm and oem
            custom_oem_psm_config = r'--oem ' + str(
                self.oem) + r' --psm ' + str(self.psm)
            d = pytesseract.image_to_data(current_page,
                                          self.language,
                                          config=custom_oem_psm_config,
                                          output_type=Output.DICT)
            no_of_boxes = (len(d['left']))

            for t in range(no_of_boxes):
                # to get rid of empty boxes
                if len(d['text'][t]) != 0:
                    text = d['text'][t]
                    x1 = d['left'][t]
                    y1 = d['top'][t]
                    x2 = d['left'][t] + d['width'][t]
                    y2 = d['top'][t] + d['height'][t]

                    # noinspection PyDictCreation
                    output_dict = {
                        "bbox": {
                            "x1": None,
                            "y1": None,
                            "x2": None,
                            "y2": None
                        },
                        "text": None,
                        "page": None
                    }

                    output_dict["bbox"]["x1"] = x1
                    output_dict["bbox"]["y1"] = y1
                    output_dict["bbox"]["x2"] = x2
                    output_dict["bbox"]["y2"] = y2
                    output_dict["text"] = text
                    output_dict["page"] = current_page_num

                    output_list.append(output_dict)

        # writing json output
        json_output = json.dumps(output_list, indent=4)
        jsonFile = open('data.json', 'w')
        jsonFile.write(json_output)
        jsonFile.close()

        # delete the last current_page.jpg
        os.remove('current_page.jpg')

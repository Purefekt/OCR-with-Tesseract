import pytesseract


class basic_ocr:

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

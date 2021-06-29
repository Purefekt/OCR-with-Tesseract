import pytesseract


class OCR:

    def __init__(self, input_path, language, oem, psm):
        self.input_path = input_path
        self.language = language
        self.oem = oem
        self.psm = psm

    def ocr_output(self):
        custom_oem_psm_config = r'--oem ' + str(self.oem) + r' --psm ' + str(
            self.psm)
        output = pytesseract.image_to_string(self.input_path,
                                             lang=self.language,
                                             config=custom_oem_psm_config)
        return output

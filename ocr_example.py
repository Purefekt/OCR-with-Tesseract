from ocr.ocr import ocr

test_image = '/Users/veersingh/Desktop/Internship/data-extraction/assets/basic_ocr.png'
test_image_language = 'hin'

test_pdf = '/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf_test.pdf'
test_pdf_language = 'eng'

oem = 3
psm = 3

# Testing basic ocr on single image
print(ocr(test_image, test_image_language, oem, psm).basic_ocr())

# Testing ocr on pdf.
ocr(test_pdf, test_pdf_language, oem, psm).ocr_on_pdf()
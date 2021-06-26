from pdf2image import convert_from_path

pdf = '/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf_test.pdf'  # path to pdf
pages = convert_from_path(pdf, 350)

i = 1
for page in pages:
    image_name = "/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf2image_out/Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1

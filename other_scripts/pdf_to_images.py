from pdf2image import convert_from_path

pdf = '/Users/veersingh/Desktop/Internship/data-extraction/assets/pdf_test.pdf'
images = convert_from_path(pdf)

for i in range(len(images)):
    images[i].save('page' + str(i+1) + '.jpg', 'JPEG')

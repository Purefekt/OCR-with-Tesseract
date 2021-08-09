import os
"""
Dataset Used: Tobacco800 http://tc11.cvc.uab.es/datasets/Tobacco800_1
This dataset has 1290 scanned pages of documents containing printed text, signatures and logos. All images do not have
a signature, this is also defined in the ground truth data. This script goes through the ground truth xml files and 
flags and removes the xml and the image files for which there is no signature in the image. There were 776 such images.
New dataset is here: https://www.kaggle.com/veersingh230799/docs-with-signature
"""

ground_truth_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_xml/'
scanned_page_images_dir = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/scanned_page_images/'

total = 0
usable = 0
for filename in os.listdir(ground_truth_dir):
    total = total + 1
    # image file of the ground truth xml file
    corresponding_image_file_name = filename.replace('.xml', '.tif')
    corresponding_image_file_path = scanned_page_images_dir + corresponding_image_file_name

    current_file_path = ground_truth_dir + filename
    fhand = open(current_file_path, 'r')
    read_file = fhand.read()
    # if file contains this string, then the image has a signature. If not then delete the xml and tif files
    check_string = 'DLSignature'
    if check_string in read_file:
        usable = usable + 1
    else:
        os.remove(current_file_path)
        os.remove(corresponding_image_file_path)
    fhand.close()

print(total)
print(usable)





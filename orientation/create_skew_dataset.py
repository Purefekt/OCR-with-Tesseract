import cv2
import random
import json

img = cv2.imread(
    '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/0.jpg')
output_dir = '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/'

# initialise the dict with original image at 0 degree angle
angle_values_dict = {'0.jpg': 0}

rows = img.shape[0]
cols = img.shape[1]
img_center = (cols / 2, rows / 2)

for i in range(40):
    # get random angle between -20 and 20 upt 2 decimals
    angle = round(random.uniform(-20, 20), 2)
    M = cv2.getRotationMatrix2D(img_center, -angle, 1)
    # rotate image at the angle and set background to white
    rotated_image = cv2.warpAffine(img,
                                   M, (cols, rows),
                                   borderMode=cv2.BORDER_CONSTANT,
                                   borderValue=(255, 255, 255))
    # add text to the image
    rotated_image = cv2.putText(img=rotated_image,
                                text='rotated angle = ' + str(angle),
                                org=(25, 25),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=1,
                                color=(255, 0, 0),
                                thickness=2)

    # create output images
    file_name = str(i + 1) + '.jpg'
    file_path = output_dir + file_name
    cv2.imwrite(file_path, rotated_image)

    # write to dictinary
    angle_values_dict.update({file_name: angle})

# writing json output
json_output = json.dumps(angle_values_dict, indent=4)
output_json_file = output_dir + 'angle_values.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()

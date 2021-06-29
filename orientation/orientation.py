import cv2
import json


def get_angle(cvImage):
    """This function returns the angle at which the image is skewed at upto 2 decimals"""
    # Preprocessing
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)

    # Gives a list of contours, sort it from largest to smallest
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST,
                                           cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Largest contour is the first one in the list. minAreaRect gives the smallest area rectangle for the contour
    largestContour = contours[0]
    minAreaRect = cv2.minAreaRect(largestContour)

    # angle is the third element of minAreaRect
    angle = minAreaRect[2]

    # Calculate the skew angle
    if angle > 45:
        angle = 90 - angle
    else:
        angle = -angle
    return round((-1.0 * angle), 2)


# Load the dictionary
f = open(
    '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/angle_values.json',
)
angle_values = json.load(f)
f.close()

input_directory = '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/'

for i in range(1, 41):
    # Read all images one by one
    input_image = cv2.imread(input_directory + str(i) + '.jpg')
    # Run get_angle function to calculate the skew angle
    skew_angle = get_angle(input_image)
    # True angle from the json file
    true_angle = angle_values[str(i) + '.jpg']
    percent_difference = round(
        abs(((skew_angle - true_angle) / true_angle) * 100), 2)

    print('Image #' + str(i) + ' |real angle = ' + str(true_angle) +
          ' |calculated angle = ' + str(skew_angle) + ' |difference = ' +
          str(percent_difference) + '%')

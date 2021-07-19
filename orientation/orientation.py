import cv2
import json


def get_angle(input_image_path):
    """Calculates the angle of rotation if any on an image, like scanned documents scanned at a wrong angle

    Args:
        input_image_path: absolute path of the image we want to create the dataset with

    Returns:
        Flaot value to 2 decimal places of the calculated angle of rotation. For example: -13.05
    """
    # Preprocessing
    input_image = cv2.imread(input_image_path)
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
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


def test_accuracy():
    """Compares the calculated angle values against the actual values and gives the %age difference

    Returns:
        Prints the Image number, actual angle, calculated angle and %age difference between these values. For example:
        Image #1 |real angle = 4.72 |calculated angle = 4.74 |difference = 0.42%
    """
    # Load the actual angle values from json file
    f = open(
        '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/angle_values.json',
    )
    actual_angle_values = json.load(f)
    f.close()

    input_dir = '/Users/veersingh/Desktop/Dataset - pdf at angles from -20 to 20/'
    number_of_images = 35

    # Loop through all images, calculate angle then compare with actual angle
    for i in range(1, number_of_images + 1):
        # Read all images one by one
        input_image_path = input_dir + str(i) + '.jpg'
        # Run get_angle function to calculate the angle for each image
        calculated_angle = get_angle(input_image_path)
        # Get the actual angle value from the dictionary
        actual_angle = actual_angle_values[str(i) + '.jpg']

        # Calculates the % difference between actual and calculated values
        percent_diff = round(
            abs(((calculated_angle - actual_angle) / actual_angle) * 100), 2)

        print('Image #' + str(i) + ' |real angle = ' + str(actual_angle) +
              ' |calculated angle = ' + str(calculated_angle) +
              ' |difference = ' + str(percent_diff) + '%')


# Run
test_accuracy()

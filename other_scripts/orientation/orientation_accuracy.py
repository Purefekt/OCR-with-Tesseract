import cv2
import json
import matplotlib.pyplot as plt


def get_angle(input_image_path):
    # Preprocessing
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(input_image, (9, 9), 0)
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


def test_accuracy(actual_angle_values_json, dataset_dir, no_of_images):
    # Load the actual angle values from json file
    f = open(actual_angle_values_json,)
    actual_angle_values = json.load(f)
    f.close()

    # For plotting
    X = list()
    Y = list()

    # Loop through all images, calculate angle then compare with actual angle
    for i in range(1, no_of_images + 1):
        # Read all images one by one
        input_image_path = dataset_dir + str(i) + '.jpg'
        # Run get_angle function to calculate the angle for each image
        calculated_angle = get_angle(input_image_path)
        # Get the actual angle value from the dictionary
        actual_angle = actual_angle_values[str(i) + '.jpg']

        # Calculates the % difference between actual and calculated values
        try:
            percent_diff = round(
                abs(((calculated_angle - actual_angle) / actual_angle) * 100),
                2)
        except:
            # if actual_angle = 0
            percent_diff = 0.0

        print('Image #' + str(i) + ' |real angle = ' + str(actual_angle) +
              ' |calculated angle = ' + str(calculated_angle) +
              ' |difference = ' + str(percent_diff) + '%')

        # Plotting
        X.append(actual_angle)
        Y.append(percent_diff)

    plt.scatter(X, Y)
    plt.xlabel('Angles')
    plt.ylabel('Percentage Difference b/w Actual Angle and Calculated Angle')
    plt.show()


# Run
dataset_dir = 'orientation_dataset/'
actual_angle_values_json = 'orientation_dataset/angle_values.json'
no_of_images = 1400

test_accuracy(actual_angle_values_json, dataset_dir, no_of_images)

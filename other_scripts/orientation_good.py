import cv2


# Calculate skew angle of an image
def getSkewAngle(cvImage):
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)
    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # get the largest contour and its angle to be rotated
    largestContour = contours[0]
    minAreaRect = cv2.minAreaRect(largestContour)
    print(minAreaRect)

    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[2]
    if angle < -45:
        angle = 90 + angle
        print('check')
    angle_to_rotate = -1.0 * angle
    print(angle_to_rotate)



img = cv2.imread('/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img_skew_65.PNG')
getSkewAngle(img)

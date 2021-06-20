def opening(self):
    """opening performs erosion then dilation and is less destructive, after grayscale"""
    gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
    # 5x5 kernal of all ones
    kernel = np.ones((5, 5), np.uint8)
    opening_morph = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    return cv2.imshow('Opening', opening_morph)


def canny(self):
    """canny edge detection, after grayscale"""
    gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
    canny_edge = cv2.Canny(gray, 100, 200)
    return cv2.imshow('Canny Edge', canny_edge)
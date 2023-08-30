import cv2
import numpy as np

PATH = 'sample.jpg' # path to the image

image = cv2.imread(PATH)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 1. Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 2. Canny Edge Detection
circles = cv2.HoughCircles(
    blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=100
)

# 3. Draw Circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        area = np.pi * radius ** 2 # calculate the area, but the unit is pixel, not a real world unit

        cv2.circle(image, center, radius, (0, 255, 0), 2) # draw the outer circle in green
        cv2.putText(image, f"Area: {area:.2f}", (circle[0], circle[1] + radius + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA) # put text in black

cv2.imshow('Circles with Areas', image) # show the image
cv2.waitKey(0) # wait for a key press
cv2.destroyAllWindows() # close all windows

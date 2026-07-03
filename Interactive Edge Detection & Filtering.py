import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Image3.jpeg')
if image is None:
    print("Error: Could not read the image.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def nothing(x):
    pass
cv2.namedWindow("Edge Detection & Filtering")
cv2.createTrackbar("Gaussian" , "Image Processing", 1, 20, nothing)
cv2.createTrackbar("Median" , "Image Processing", 1, 20, nothing)
cv2.createTrackbar("Sobel" , "Image Processing", 1, 7, nothing)
cv2.createTrackbar("Laplacian" , "Image Processing", 1, 31, nothing)
cv2.createTrackbar("Canny Min" , "Image Processing", 50, 255, nothing)
cv2.createTrackbar("Canny Max" , "Image Processing", 150, 255, nothing)
while True:
    g = cv2.getTrackbarPos("Gaussian", "Image Processing")
    m = cv2.getTrackbarPos("Median", "Image Processing")
    s = cv2.getTrackbarPos("Sobel", "Image Processing")
    l = cv2.getTrackbarPos("Laplacian", "Image Processing")
    c_min = cv2.getTrackbarPos("Canny Min", "Image Processing")
    c_max = cv2.getTrackbarPos("Canny Max", "Image Processing")
    g = max(1, g * 2 + 1)
    if g % 2 == 0:
        g += 1
    m = max(1, m * 2 + 1)
    if m % 2 == 0:
        m += 1
    s = max(1, s * 2 + 1)
    if s % 2 == 0:
        s += 1
    l = max(1, l * 2 + 1)
    if l % 2 == 0:
        l += 1
    gaussian_blurred = cv2.GaussianBlur(gray_image, (g, g), 0)
    median_blurred = cv2.medianBlur(gray_image, m)
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=s)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=s)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=l)
    laplacian = np.uint8(np.absolute(laplacian))
    canny_edges = cv2.Canny(gray_image, c_min, c_max)
    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Gaussian Blurred", gaussian_blurred)
    cv2.imshow("Median Blurred", median_blurred)
    cv2.imshow("Sobel Edge Detection", cv2.convertScaleAbs(sobelx) + cv2.convertScaleAbs(sobely))
    cv2.imshow("Laplacian Edge Detection", laplacian)
    cv2.imshow("Canny Edge Detection", canny_edges)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
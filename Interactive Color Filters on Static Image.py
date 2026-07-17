import cv2
import numpy as np
image = cv2.imread("Image3.jpeg")
if image is None:
    print("Error: image.jpg not found!")
    exit()
original = image.copy()
current = original.copy()
print("=" * 50)
print("REAL-TIME IMAGE COLOR MANIPULATOR")
print("=" * 50)
print("R - Red Filter")
print("G - Green Filter")
print("B - Blue Filter")
print("Y - Yellow Tint")
print("C - Cyan Tint")
print("M - Magenta Tint")
print("+ - Increase Brightness")
print("- - Decrease Brightness")
print("N - Original Image")
print("ESC - Exit")
print("=" * 50)
while True:
    cv2.imshow("Color Channel Manipulator", current)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('r'):
        current = original.copy()
        current[:, :, 1] = 0
        current[:, :, 0] = 0
    elif key == ord('g'):
        current = original.copy()
        current[:, :, 2] = 0
        current[:, :, 0] = 0
    elif key == ord('b'):
        current = original.copy()
        current[:, :, 2] = 0
        current[:, :, 1] = 0
    elif key == ord('y'):
        current = original.copy()
        current[:, :, 0] = 0
    elif key == ord('c'):
        current = original.copy()
        current[:, :, 2] = 0
    elif key == ord('m'):
        current = original.copy()
        current[:, :, 1] = 0
    elif key == ord('+') or key == ord('='):
        current = cv2.convertScaleAbs(current, alpha=1, beta=30)
    elif key == ord('-'):
        current = cv2.convertScaleAbs(current, alpha=1, beta=-30)
    elif key == ord('n'):
        current = original.copy()
    elif key == 27:
        break
cv2.destroyAllWindows()
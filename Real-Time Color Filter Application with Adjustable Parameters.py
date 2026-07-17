import cv2
import numpy as np
image = cv2.imread("Image3.jpeg")
if image is None:
    print("Image not found.")
    exit()
red = 1.0
green = 1.0
blue = 1.0
saved_count = 1
while True:
    img = image.astype(np.float32)
    img[:, :, 0] *= blue
    img[:, :, 1] *= green
    img[:, :, 2] *= red
    img = np.clip(img, 0, 255).astype(np.uint8)
    cv2.putText(img, f"R:{red:.1f} G:{green:.1f} B:{blue:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imshow("Real-Time Color Filter", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        red = min(red + 0.1, 3.0)
    elif key == ord('f'):
        red = max(red - 0.1, 0.0)
    elif key == ord('g'):
        green = min(green + 0.1, 3.0)
    elif key == ord('t'):
        green = max(green - 0.1, 0.0)
    elif key == ord('b'):
        blue = min(blue + 0.1, 3.0)
    elif key == ord('v'):
        blue = max(blue - 0.1, 0.0)
    elif key == ord('1'):
        red, green, blue = 2.0, 1.0, 1.0
    elif key == ord('2'):
        red, green, blue = 1.0, 2.0, 1.0
    elif key == ord('3'):
        red, green, blue = 1.0, 1.0, 2.0
    elif key == ord('4'):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Real-Time Color Filter", gray)
        cv2.waitKey(1)
    elif key == ord('5'):
        negative = 255 - img
        cv2.imshow("Real-Time Color Filter", negative)
        cv2.waitKey(1)
    elif key == ord('0'):
        red = 1.0
        green = 1.0
        blue = 1.0
    elif key == ord('s'):
        filename = f"filtered_image_{saved_count}.png"
        cv2.imwrite(filename, img)
        print(filename, "saved.")
        saved_count += 1
    elif key == 27:
        break
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('Image3.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title('Rotated Image')
plt.axis('off')
plt.show()
cropped = image[50:300, 50:300]
cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title('Cropped Image')
plt.axis('off')
plt.show()
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title('Brighter Image')
plt.axis('off')
plt.show()
mirrored = cv2.flip(image, 1)
mirrored_rgb = cv2.cvtColor(mirrored, cv2.COLOR_BGR2RGB)
plt.imshow(mirrored_rgb)
plt.title('Mirrored Image')
plt.axis('off')
plt.show()
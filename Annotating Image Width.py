import cv2
import matplotlib.pyplot as plt
image = cv2.imread("Image csv.jpg")
if image is None:
    print("Error: Could not read the image.")
    exit()
height, width, channels = image.shape
cv2.rectangle(image, (50, 50), (250, 200), (0, 255, 0), 2)
cv2.circle(image, (400, 150), 50, (255, 0, 0), 2)
cv2.line(image, (250, 125), (350, 150), (0, 0, 255), 2)
y = height - 40
cv2.arrowedLine(
    image,
    (width // 2, y),
    (20, y),
    (255, 255, 0),
    2,
    tipLength=0.03
)
cv2.arrowedLine(
    image,
    (width // 2, y),
    (width - 20, y),
    (255, 255, 0),
    2,
    tipLength=0.03
)
cv2.putText(
    image,
    f"Width = {width} pixels",
    (width // 2 - 90, y - 15),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 255),
    2
)
cv2.putText(
    image,
    f"Height = {height} pixels",
    (20, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2
)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.title("Image Width Measurement Using Bi-Directional Arrows")
plt.axis("off")
plt.show()
cv2.imwrite("annotated_image.jpg", image)
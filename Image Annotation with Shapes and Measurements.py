import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Image csv.jpg')
if image is None:
    print("Could not read the image.")
    exit()
height, width, channels = image.shape
cv2.rectangle(image , (50 , 50) , (200 , 200) , (0 , 255 , 0) , 2)
cv2.circle(image , (350 , 150) , 50 , (255 , 0 , 0) , 3)
cv2.line(image , (200 , 125) , (300 , 150) , (0 , 0 , 255) , 2)
cv2.arrowedLine(image , (width - 50 , height - 10) , (width - 50 , height - 50) , (0 , 255 , 255) , 2 , tipLength = 0.03)
cv2.putText(image , "Rectangle ROI" , (40 , 40) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (0 , 255 , 0) , 2)
cv2.putText(image , "Circle ROI" , (300 , 40) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (255 , 0 , 0) , 2)
cv2.putText(image , f"height = {height}px" , (width - 200 , height//2) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (255 , 255 , 0) , 2)
plt.figure(figsize = (12 , 8))
plt.imshow(image)
plt.show()
#cv2.imshow('Annotated Image' , image)
#cv2.waitKey(15)
#cv2.destroyAllWindows()
#cv2.imwrite('Annotated_Image.jpg' , image)
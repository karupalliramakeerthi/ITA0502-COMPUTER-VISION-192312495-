import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Please upload image.jpg")

rotated = cv2.rotate(img, cv2.ROTATE_180)

plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title("180 Degree Clockwise Rotation")
plt.axis("off")
plt.show()

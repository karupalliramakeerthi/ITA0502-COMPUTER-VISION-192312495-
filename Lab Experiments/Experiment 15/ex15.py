import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Please upload image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)

result = img.copy()
result[corners > 0.01 * corners.max()] = [0, 0, 255]

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.axis("off")
plt.show()

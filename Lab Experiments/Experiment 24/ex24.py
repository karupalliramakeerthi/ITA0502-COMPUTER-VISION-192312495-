import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Upload image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)

result = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

plt.imshow(result, cmap="gray")
plt.title("Black-Hat Transformation")
plt.axis("off")
plt.show()

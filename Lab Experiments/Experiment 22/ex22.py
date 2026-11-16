import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Upload image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

plt.imshow(result, cmap="gray")
plt.title("Morphological Closing")
plt.axis("off")
plt.show()

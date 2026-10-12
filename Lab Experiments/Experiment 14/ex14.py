import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Please upload image.jpg")

h, w = img.shape[:2]

src = np.float32([
    [0, 0],
    [w - 1, 0],
    [w - 1, h - 1],
    [0, h - 1]
])

dst = np.float32([
    [w * 0.1, h * 0.1],
    [w * 0.9, h * 0.05],
    [w * 0.8, h * 0.9],
    [w * 0.2, h * 0.85]
])

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (w, h))

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Perspective Transformation")
plt.axis("off")
plt.show()

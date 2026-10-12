import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Please upload image.jpg")

h, w = img.shape[:2]

src = np.float32([[0, 0], [w - 1, 0], [0, h - 1]])
dst = np.float32([[50, 50], [w - 51, 30], [30, h - 51]])

matrix = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, matrix, (w, h))

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Affine Transformation")
plt.axis("off")
plt.show()

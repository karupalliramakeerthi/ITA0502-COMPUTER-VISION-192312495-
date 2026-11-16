import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Upload image.jpg")

h, w = img.shape[:2]

x, y = w // 4, h // 4
roi_w, roi_h = w // 4, h // 4

roi = img[y:y + roi_h, x:x + roi_w].copy()
result = img.copy()

paste_x, paste_y = w - roi_w, h - roi_h
result[paste_y:h, paste_x:w] = roi

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("ROI Copied and Pasted")
plt.axis("off")
plt.show()

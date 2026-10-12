import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Please upload image.jpg")

height, width = img.shape[:2]

bigger = cv2.resize(img, (width * 2, height * 2),
                    interpolation=cv2.INTER_CUBIC)
smaller = cv2.resize(img, (width // 2, height // 2),
                     interpolation=cv2.INTER_AREA)

plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
plt.title("Bigger Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
plt.title("Smaller Image")
plt.axis("off")

plt.tight_layout()
plt.show()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Upload image.jpg")

watermark = img.copy()
h, w = img.shape[:2]

cv2.putText(watermark, "WATERMARK",
            (max(10, w // 20), max(30, h - 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2, cv2.LINE_AA)

result = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

cv2.imwrite("watermarked.jpg", result)

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Watermarked Image")
plt.axis("off")
plt.show()

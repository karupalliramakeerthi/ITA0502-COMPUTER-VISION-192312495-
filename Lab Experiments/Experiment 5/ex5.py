import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Please upload image.jpg")

    colors = ("b", "g", "r")
    labels = ("Blue", "Green", "Red")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=labels[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()

analyze_histogram("image.jpg")

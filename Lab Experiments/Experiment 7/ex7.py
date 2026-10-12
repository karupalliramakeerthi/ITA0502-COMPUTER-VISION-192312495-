import cv2

path = r"C:\Users\User\OneDrive\Desktop\Image_Processing\video.mp4.mp4"

video = cv2.VideoCapture(path)

print("Video opened:", video.isOpened())

if video.isOpened():
    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Video Output", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
else:
    print("Video could not be opened")

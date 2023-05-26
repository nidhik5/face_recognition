import cv2

# initialize video capture object
cap = cv2.VideoCapture(0)

while True:
    # read frame from video capture object
    ret, frame = cap.read()

    # show the frame in a window
    cv2.imshow('Video', frame)

    # wait for 'q' key to be pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

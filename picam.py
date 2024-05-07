import cv2
from picamera2 import PiCamera
from picamera2.array import PiRGBArray
import time

# Create a PiCamera object
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

# Create a PiRGBArray object
raw_capture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

# Capture frames from the camera
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Process the image using OpenCV (for example, convert it to grayscale)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow("Frame", gray)
    
    # Wait for key press and check if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
    # Clear the stream in preparation for the next frame
    raw_capture.truncate(0)

# Close OpenCV windows
cv2.destroyAllWindows()

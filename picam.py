import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
raw_capture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # Process the image using OpenCV (for example, you can apply some image processing)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow("Frame", gray)
    key = cv2.waitKey(1) & 0xFF

    # Clear the stream in preparation for the next frame
    raw_capture.truncate(0)

    # If the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# Close OpenCV windows
cv2.destroyAllWindows()

import cv2
from datetime import datetime as DateTime

from picamera2 import Picamera2

# Grab images as numpy arrays and leave everything else to OpenCV.

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.set_controls({"FrameRate": 200})
picam2.start()

last_frame_time = DateTime.now()
frame_rate = 0

while True:
    current_time = DateTime.now()

    frame_rate = 1 / (current_time - last_frame_time).total_seconds()
    print(frame_rate)

    last_frame_time = DateTime.now()

    im = picam2.capture_array()

    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(im, (0, 0), (100, 100), (0, 255, 0))

    cv2.imshow("Camera", im)
    cv2.waitKey(1)
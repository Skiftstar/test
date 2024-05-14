import cv2
from flask import Flask, Response
from picamera2 import Picamera2

app = Flask(__name__)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.set_controls({"FrameRate": 120})
picam2.start()

def generate_frames():
    while True:
        im = picam2.capture_array()
        grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(im, (0, 0), (100, 100), (0, 255, 0))
        ret, jpeg = cv2.imencode('.jpg', im)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
import asyncio
import websockets
import binascii
from io import BytesIO
from PIL import Image
from flask import Flask, Response
from base64 import b64encode


app = Flask(_name_)

@app.route('/')
def index():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')


def get_image():
    while True:
        try:
            with open("http://192.168.162.10/capture?_cb=1732718224999", "rb") as f:
                image_bytes = f.read()
            image = Image.open(BytesIO(image_bytes))
            img_io = BytesIO()
            image.save(img_io, 'JPEG')
            img_io.seek(0)
            img_bytes = img_io.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')

        except Exception as e:
            print("encountered an exception: ")
            print(e)

            with open("placeholder.jpg", "rb") as f:
                image_bytes = f.read()
            image = Image.open(BytesIO(image_bytes))
            img_io = BytesIO()
            image.save(img_io, 'JPEG')
            img_io.seek(0)
            img_bytes = img_io.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')
            continue

app.run(host='192.168.162.10/', debug=False, threaded=True)
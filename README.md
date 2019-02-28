# Inteligent-Camera

### Short description
An inteligent camera that detects faces and tracks them.

### Longer description
A camera that is mounted on a chassis. The chassis consists of two moving servosmotors: one used for up and down movement and one for left and right. The servosmotors are conencted to an Arduino Uno and we are using the Python module PySerial to send and receive between Python and Arduino.

Also, We are using the OpenCV Python module so we can parse the camera feed/video. We look at each frame/image and we check if there is any face detected in the image (using the haarcascade_frontalface_default classifier). For every face detected we calculate some coordinates that describe where the face is positioned in the image. Based on these coordinates we are moving the two servosmotors so we can track the face.

## Documentation in progress ...



# Inteligent-Camera

A system that detects faces and tracks them.

For hardware, we have a camera that is mounted on a chassis which mainly consists of two moving servomotors: one used for the vertical and the other one for the horizontal movement of the camera. These 2 servomotors are connected to an Arduino Uno board.

On the software side, I'm using Python:
- to get the input from the camera (video/images), with the help of the OpenCV library;
- to send and receive data to the Arduino board using the PySerial library;
and C/C++ code (.ino file) for the Arduino board in order to set up and move the servomotors.

Getting into more detail, using the OpenCV I check each image/frame we take a look at each frame/image and we check if there is any face detected in it. For every face detected we calculate some coordinates that describe where the face is positioned in the image compared to its center. Based on these coordinates we are moving the two servomotors so we can track the face.

## Documentation in progress ...



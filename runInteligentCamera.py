from camera import Camera
from connection import Connection
import cv2
import time



def main():

    arduinoSerial = Connection('COM3', 115200, 2)

    userInput = input("Do you want to use potentiometer or intelligent camera; "
                      "Type I for intelligent camera; Type P for potentiometer")

    if userInput == 'I' or userInput == 'i':

        PIRsensor = arduinoSerial.readData()
        while PIRsensor != 'B':
            PIRsensor = arduinoSerial.readData()
            time.sleep(1)

        videoCamera = Camera(1)

        # Read until video is completed
        while (videoCamera.videoCapture.isOpened()):
            time.sleep(0.01)

            # Capture frame-by-frame
            returnBool, frame = videoCamera.getCameraFrame()

            if returnBool:

                centers = []

                frameFacesDrawn, centers = videoCamera.detectFaces(frame)
                videoCamera.showFrame(frameFacesDrawn)

                if len(centers) != 0:
                    for (x, y) in centers:
                        serialOutput = "X{0:d}Y{1:d}".format(x, y)
                        arduinoSerial.sendData(serialOutput)
                else:
                    arduinoSerial.sendData(('L'))
                    print("nothing detected")
                # Press Q on keyboard to  exit
                if cv2.waitKey(33) & 0xFF == ord('q'):
                    arduinoSerial.sendData('q')
                    break

            # Break the loop
            else:
                break

    elif userInput == 'P' or userInput == 'p':
        while True:
            arduinoSerial.sendData("P")

    videoCamera.cleanup()


main()

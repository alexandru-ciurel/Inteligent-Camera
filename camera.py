import cv2

class Camera:

    def __init__(self, cameraNumber, path='haarcascade_frontalface_default.xml', window='videoWindow'):
        self.videoCapture = cv2.VideoCapture(cameraNumber)
        self.pathXML = path
        self.classfier = cv2.CascadeClassifier(self.pathXML)
        self.window = window
        cv2.namedWindow(self.window)
        cv2.moveWindow(self.window, 0, 0)

    def getCameraFrame(self):
        boolReturn, frame = self.videoCapture.read()
        return boolReturn, frame

    def showFrame(self, frame):
        cv2.imshow(self.window, frame)

    def cleanup(self):
        self.videoCapture.release()
        cv2.destroyAllWindows()

    def detectFaces(self, frame):
        # global previousX, previousY, minXX, minYY

        cascade = self.classfier
        image_copy = frame.copy()

        # convert the test image to gray scale as opencv face detector expects gray images
        gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

        # Applying the haar classifier to detect faces
        facesDetected = cascade.detectMultiScale(gray_image, scaleFactor = 2, minNeighbors = 5)

        #minimumdistance = 800

        centers = []

        if len(facesDetected) != 0:
            print(facesDetected)
            for (x, y, w, h) in facesDetected:
                cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 100), 5)

                # Center of the rectangle
                cv2.line(image_copy, (x + int(1 / 2 * w), y + int(1 / 2 * h)), (x + int(1 / 2 * w), y + int(1 / 2 * h)),
                         (0, 0, 255), 7)

                xx = x + int(1 / 2 * w)
                yy = y + int(1 / 2 * h)
                centers.append((xx, yy))

        return image_copy, centers


'''
                print(xx, yy, previousX, previousY)

                # The next part of code is for when we have multiple faces detected in our frame
                # We store the values for the previous detected face in previousX and previousY
                #

                if xx - 20 > previousX and yy - 20 > previousY:
                    print('break')
                    break

                distance = math.sqrt(((xx - previousX) ** 2) + ((previousY - yy) ** 2))

                if distance < minimumdistance:
                    minXX = xx
                    minYY = yy
                    minimumdistance = distance

                minimumdistance = min(minimumdistance, distance)
            previousX = xx
            previousY = yy
            serialOutput = "X{0:d}Y{1:d}".format(minXX, minYY)
            arduinoSerial.write(str.encode(serialOutput))
        else:
            arduinoSerial.write(str.encode('L'))
            print("nothing detected")
        return image_copy


'''

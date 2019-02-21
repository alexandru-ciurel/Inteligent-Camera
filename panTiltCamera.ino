#include <Servo.h>


// Pins declaration
int potPIN = A0;
int pirPIN = 5;
int ledPIN = 6;
int panPIN = 9, tiltPIN = 8;

int prevX, prevTiltValue = 50;
int prevY, prevPanValue = 90;
int x, y;

int startingTime, currentTime, elapsedTime, timerOK = 0;
Servo pan, tilt;  // create servo object to control a servo

void setup() {
    Serial.begin(115200);
    pan.attach(panPIN);      // left -- right
    tilt.attach(tiltPIN);     // up     -- down
    pan.write(prevPanValue);
    tilt.write(prevTiltValue);
    pinMode(ledPIN, OUTPUT);
    pinMode(pirPIN, INPUT_PULLUP);
    currentTime = millis();
    startingTime = millis();
}

void loop() {

    currentTime = millis();
    
    int buttonState = digitalRead(pirPIN);
    if (buttonState == LOW) {
        //Serial.println(1);
        Serial.println("B");
        startingTime = millis();
        timerOK = 1;
    }
    
    while (timerOK == 1) {
        elapsedTime = currentTime - startingTime;
        if (elapsedTime <= 1000) {
            Serial.println("B");
            //Serial.println();
            timerOK = 0;
        }
    }
  
    if (Serial.available() > 0) {

        int serialInput = Serial.read();
        if (serialInput == 'L'){
            digitalWrite(6, LOW);
        }
        if (serialInput == 'X') {
            digitalWrite(6, HIGH);
            x = Serial.parseInt();
            serialInput = Serial.read();
            if (serialInput == 'Y') {
                y = Serial.parseInt();
                move();
            }
            else if (serialInput == 'q') {
                exit(0);
            }
        }
        else if (serialInput == 'q') {
            exit(0);
        }
        else if (serialInput == 'P') {
            potMeter();
        }
        while (Serial.available() > 0) {
            Serial.read();
        }
    }
    
}

void move() {
    if ((x < prevX + 25 || x > prevX - 25) && \
        (y < prevY + 25 || y > prevY - 25)) {
        prevX = x;
        prevY = y;

        int panValue = map(x, 0, 640 , 115, 75);
        int tiltValue = map(y, 0, 480, 50, 90);

        // Smooth panning
        if (prevPanValue < panValue) {
            while (prevPanValue < panValue) {
                pan.write(prevPanValue);
                prevPanValue += 15;
                delay (5);
            }
        }
        else {
            while (prevPanValue > panValue) {
                pan.write(prevPanValue);
                prevPanValue -= 15;
                delay (5);
            }
        }

        // Smooth tilting
        if (prevTiltValue < tiltValue) {
            while (prevTiltValue < tiltValue) {
                tilt.write(prevTiltValue);
                prevTiltValue += 10;
                delay (5);
            }
        }
        else {
            while (prevTiltValue > tiltValue) {
                tilt.write(prevTiltValue);
                prevTiltValue -= 10;
                delay (5);
            }
        }

        prevTiltValue = tiltValue;
        prevPanValue = panValue;

        delay(20);
    }
}

void potMeter() {
    int value;
    // reads the value of the potentiometer (value between 0 and 1023)
    value = analogRead(potPIN);
    // scale it to use it with the servo (value between 0 and 180)
    value = map(value, 0, 1023, 0, 180);
    // sets the servo position according to the scaled value
    pan.write(value);
    delay(15);
}

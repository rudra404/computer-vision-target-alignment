#include <Wire.h>
#include <PS2X_lib.h>
#include <Adafruit_MotorShield.h>
#include <Adafruit_MS_PWMServoDriver.h>

volatile int i;

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
PS2X ps2x;
Adafruit_Servo *Servo1 = AFMS.getServo(1);
Adafruit_Servo *Servo3 = AFMS.getServo(3);
Adafruit_Servo *Servo4 = AFMS.getServo(4);
Adafruit_DCMotor *DCMotor_1 = AFMS.getMotor(1);
Adafruit_DCMotor *DCMotor_2 = AFMS.getMotor(2);
Adafruit_DCMotor *DCMotor_3 = AFMS.getMotor(3);
Adafruit_DCMotor *DCMotor_4 = AFMS.getMotor(4);

void setup()
{
  AFMS.begin(50);
         
  int error = 0;
  do{
    error = ps2x.config_gamepad(13,11,10,12, true, true);
    if(error == 0){
      break;
    }else{
      delay(100);
    }
  }while(1); 

  i = 1;
}

void loop()
{
  ps2x.read_gamepad(false, 0);
  delay(30);
  if (ps2x.Button(PSB_PAD_UP)) {
    if (Servo1->readDegrees() < 150) {
      Servo1->writeServo((Servo1->readDegrees() + 3));delay(1);

    }

  } else if (ps2x.Button(PSB_PAD_DOWN)) {
    if (Servo1->readDegrees() > 0) {
      Servo1->writeServo((Servo1->readDegrees() - 3));delay(1);

    }
  } else if (ps2x.Button(PSB_L1)) {
    if (Servo3->readDegrees() < 90) {
      Servo3->writeServo((Servo3->readDegrees() + 3));delay(1);

    }
  } else if (ps2x.Button(PSB_L2)) {
    if (Servo3->readDegrees() > 0) {
      Servo3->writeServo((Servo3->readDegrees() - 3));delay(1);

    }
  } else if (ps2x.Button(PSB_R1)) {
    if (Servo4->readDegrees() < 120) {
      Servo4->writeServo((Servo4->readDegrees() + 3));delay(1);

    }
  } else if (ps2x.Button(PSB_R2)) {
    if (Servo4->readDegrees() > 0) {
      Servo4->writeServo((Servo4->readDegrees() - 3));delay(1);

    }
  } else if (ps2x.Analog(PSS_LY) < 10) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(FORWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(FORWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(FORWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(FORWARD);
  } else if (ps2x.Analog(PSS_LY) > 240) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(BACKWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(BACKWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(BACKWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(BACKWARD);
  } else if (ps2x.Analog(PSS_LX) < 10) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(BACKWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(FORWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(FORWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(BACKWARD);
  } else if (ps2x.Analog(PSS_LX) > 240) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(FORWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(BACKWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(BACKWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(FORWARD);
  } else if (ps2x.Analog(PSS_RX) < 10) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(BACKWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(FORWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(BACKWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(FORWARD);
  } else if (ps2x.Analog(PSS_RX) > 240) {
    DCMotor_1->setSpeed(100);
    DCMotor_1->run(FORWARD);
    DCMotor_2->setSpeed(100);
    DCMotor_2->run(BACKWARD);
    DCMotor_3->setSpeed(100);
    DCMotor_3->run(FORWARD);
    DCMotor_4->setSpeed(100);
    DCMotor_4->run(BACKWARD);
  } else {
    DCMotor_1->setSpeed(0);
    DCMotor_1->run(RELEASE);
    DCMotor_2->setSpeed(0);
    DCMotor_2->run(RELEASE);
    DCMotor_3->setSpeed(0);
    DCMotor_3->run(RELEASE);
    DCMotor_4->setSpeed(0);
    DCMotor_4->run(RELEASE);

  }
  delay(10);

}void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}

#include <QMC5883LCompass.h>
QMC5883LCompass compass;

int calibrationData[3][2];
bool changed = false;
bool done = false;
int t = 0;
int c = 0;
int x, y, z;
int motor1=12;
int motor11=11;
int motor2=10;
int motor22=9;

void setup() {
  Serial.begin(9600);

  pinMode(motor1,OUTPUT);
  pinMode(motor11,OUTPUT);
  pinMode(motor2,OUTPUT);
  pinMode(motor22,OUTPUT);

  compass.init();
  Serial.println("Calibration will begin in 5 seconds.");
  delay(5000);

  compass.read();       // Read compass values
  x = compass.getX();   // Return XYZ readings
  y = compass.getY();
  z = compass.getZ();

  changed = false;

  if(x < calibrationData[0][0]) {
    calibrationData[0][0] = x;
    changed = true;
  }
  if(x > calibrationData[0][1]) {
    calibrationData[0][1] = x;
    changed = true;
  }

  if(y < calibrationData[1][0]) {
    calibrationData[1][0] = y;
    changed = true;
  }
  if(y > calibrationData[1][1]) {
    calibrationData[1][1] = y;
    changed = true;
  }

  if(z < calibrationData[2][0]) {
    calibrationData[2][0] = z;
    changed = true;
  }
  if(z > calibrationData[2][1]) {
    calibrationData[2][1] = z;
    changed = true;
  }

  if (changed && !done) {
    Serial.println("CALIBRATING...");
    Rt(15000,15000);
    c = millis();
  }
    t = millis();
  
  
  if ( (t - c > 5000) && !done) {
    
    compass.setCalibration(calibrationData[0][0],calibrationData[0][1],calibrationData[1][0],calibrationData[1][1],calibrationData[2][0],calibrationData[2][1]);
  delay(1000);
  Serial.println("Finished calibration");
  done = true;
  }
  }


void loop() {
 compass.read();
  
  byte a = compass.getAzimuth();

  char myArray[3];
  compass.getDirection(myArray, a);
  
  Serial.print(myArray[0]);
  Serial.print(myArray[1]);
  Serial.print(myArray[2]);
  Serial.println();
  delay(250); 
  
  
 
}
void Fwd(int x, int y)
{
    digitalWrite(motor1,HIGH);
    digitalWrite(motor11,LOW);
    delay(x);
    digitalWrite(motor2,HIGH);
    digitalWrite(motor22,LOW);
    delay(y);
}


void Bck(int x, int y)
{
    digitalWrite(motor11,HIGH);
    digitalWrite(motor1,LOW);
    delay(x);
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,HIGH);
    delay(y);
}

void Lft(int x, int y)
{
    digitalWrite(motor1,HIGH);
    digitalWrite(motor11,LOW);
    delay(x);
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,HIGH);
    delay(y);
}

void Rt(int x, int y)
{
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,HIGH);
    delay(x);
    digitalWrite(motor2,HIGH);
    digitalWrite(motor22,LOW);
    delay(y);
}
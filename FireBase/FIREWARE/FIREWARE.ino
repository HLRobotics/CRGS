#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

#define FIREBASE_HOST "swarm-98ef3-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "lLEj9s4UtbnzAdMTYVcqtwdu0yNSSaLWvXHL7l9T"
#define WIFI_SSID "INKER_ROBOTICS.....!!!!!"
#define WIFI_PASSWORD "Inker@2020"

int motor1=D8;
int motor11=D7;
int motor2=D6;
int motor22=D5;

int led=D0;
int led2=D1;
int led3=D2;
String action;
String previous_action;
void setup()
{ 
  
  Serial.begin(9600);
  pinMode(D8,OUTPUT);
  pinMode(D7,OUTPUT);
  pinMode(D6,OUTPUT);
  pinMode(D5,OUTPUT);
  
  pinMode(D2,OUTPUT);
  pinMode(D1,OUTPUT);
  pinMode(D0,OUTPUT);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting"); 
   
  while (WiFi.status() != WL_CONNECTED)
  {
  Serial.print(".");
  digitalWrite(led,HIGH);
  delay(500);
  digitalWrite(led,LOW);
  delay(500);
  }
  if(WiFi.status()==WL_CONNECTED)
  {
    digitalWrite(led,LOW);
    digitalWrite(led1,HIGH);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}
void firebasereconnect()
{
  Serial.println("Trying to reconnect");
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  digitalWrite(led,LOW);
  digitalWrite(led2,HIGH);
}
void loop()
{
  if (Firebase.failed())
  {
      Serial.print("setting number failed:");
      Serial.println(Firebase.error());  
      firebasereconnect();
      digitalWrite(led,HIGH);
      digitalWrite(led2,LOW);
      return;
  }
    int ControllerDelay=550;
    //Serial.println(ControllerDelay);
    action=Firebase.getString("direction/Direction");
    action.trim();
    int steps1=(100*(((action[1]-48)*100)+((action[2]-48)*10)+(action[3]-48)));
    int steps2=100*(((action[5]-48)*100)+((action[6]-48)*10)+(action[7]-48));
    //Serial.println(steps1);
    Serial.println("[MESSAGE RECEIVED BY NODEMCU]");
    Serial.println(action);
    Serial.println("[PROCESSING]");
    delay(2000);
    
    if(action=="ON")
    {
      digitalWrite(D4,HIGH);
    }
    else if(action=="OFF")
    {
      digitalWrite(D4,LOW);
    }
    if(previous_action==action)
    {
      Serial.println("[AT THE DESTINATION]");
      digitalWrite(motor1,LOW);
      digitalWrite(motor11,LOW);    
      digitalWrite(motor2,LOW);
      digitalWrite(motor22,LOW);
      digitalWrite(led3,HIGH);
      delay(200);
      digitalWrite(led3,LOW);
      delay(500);
    }
    else
    {
    if(action[0]=='F')
    {
        digitalWrite(D4,HIGH);
        Fwd(steps1);
        if(action[4]=='R')
        {
           msg2Rt(ControllerDelay,steps2); 
           Lt(ControllerDelay);
        }
        else if(action[4]=='L')
        {
            msg2Lt(ControllerDelay,steps2);
            Rt(ControllerDelay);
        }
        else if(action[4]=='F')
        {
          Fwd(steps2);  
        }
        Serial.println("[REACHED DESTINATION]");
        digitalWrite(D4,LOW);
    }
    else if(action[0]=='L')
    {
       digitalWrite(D4,HIGH);
       msg1Lt(ControllerDelay,steps1,steps2);
       Serial.println("[REACHED DESTINATION]");
       digitalWrite(D4,LOW);
    }
    else if(action[0]=='R')
    {
       digitalWrite(D4,HIGH);
       msg1Rt(ControllerDelay,steps1,steps2); 
       Serial.println("[REACHED DESTINATION]");  
       digitalWrite(D4,LOW);
    } 
    
    previous_action=action;
}}
void Fwd(int x)
{   
    
    digitalWrite(motor1E,HIGH);
    digitalWrite(motor2E,HIGH); 
    Serial.print("[MOVING FORWARD ");
    Serial.print(x/100);
    Serial.println(" STEPS]");
    digitalWrite(motor1,HIGH);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,HIGH);
    digitalWrite(motor22,LOW);
    delay(x);
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,LOW); 
    
}
void Rt(int x)
{   
    digitalWrite(motor1E,HIGH);
    digitalWrite(motor2E,HIGH);   
    Serial.println("[TURNING RIGHT]"); 
    digitalWrite(motor1,HIGH);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,HIGH);
    delay(x);
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,LOW);   
}
void Lt(int x)
{   
    digitalWrite(motor1E,HIGH);
    digitalWrite(motor2E,HIGH); 
    Serial.println("[TURNING LEFT]");
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,HIGH);    
    digitalWrite(motor2,HIGH);
    digitalWrite(motor22,LOW);
    delay(x);
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,LOW);
}
void msg1Lt(int ControllerDelay,int steps1,int steps2)
{
        Lt(ControllerDelay);
        Fwd(steps1);
        if(action[4]=='R')
        {
           msg2Rt(ControllerDelay,steps2); 
        }
        else if(action[4]=='L')
        {
            msg2Lt(ControllerDelay,steps2);
            Rt(ControllerDelay*2);
        }
        else if(action[4]=='F')
        {
          Fwd(steps2);  
          Rt(ControllerDelay);
        }
}
void msg1Rt(int ControllerDelay,int steps1,int steps2)
{
        Rt(ControllerDelay);
        Fwd(steps1);
        if(action[4]=='R')
        {
           msg2Rt(ControllerDelay,steps2); 
           Lt(ControllerDelay*2);
        }
        else if(action[4]=='L')
        {
            msg2Lt(ControllerDelay,steps2);
        }
        else if(action[4]=='F')
        {
          Fwd(steps2);  
          Lt(ControllerDelay);
        }
}
void msg2Rt(int ControllerDelay,int steps2)
{
    Rt(ControllerDelay);
    Fwd(steps2);
}
void msg2Lt(int ControllerDelay,int steps2)
{           
    Lt(ControllerDelay);
    Fwd(steps2);
}
    
    
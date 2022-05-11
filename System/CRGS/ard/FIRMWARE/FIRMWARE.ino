int motor1=11;
int motor11=10;
int motor2=9;
int motor22=6;
String action;
void setup()
{
    Serial.begin(9600);
    pinMode(11,OUTPUT);
    pinMode(10,OUTPUT);
    pinMode(9,OUTPUT);
    pinMode(6,OUTPUT);
}

void loop()
{
    int ControllerDelay=127+analogRead(A7);
    Serial.println(ControllerDelay);
    action=Serial.readString();
    action.trim();
    //Serial.println(action[0]);
    int steps1=100*(((action[1]-48)*100)+((action[2]-48)*10)+(action[3]-48));
    int steps2=100*(((action[5]-48)*100)+((action[6]-48)*10)+(action[7]-48));
    Serial.println("[MESSAGE RECEIVED BY NODEMCU]");
    Serial.println(action[]);
    Serial.println("[PROCESSING]")
    if(action[0]=='F')
    {
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
    }
    else if(action[0]=='B')
    {
        Bck(steps1);
        if(action[4]=='R')
        {
           msg2Rt(ControllerDelay,steps2); 
        }
        else if(action[4]=='L')
        {
            msg2Lt(ControllerDelay,steps2);
        }
        else if(action[4]=='F')
        {
          Fwd(steps2);  
        }
    } 
    else if(action[0]=='L')
    {
       msg1Lt(ControllerDelay,steps1,steps2);
    }
    else if(action[0]=='R')
    {
       msg1Rt(ControllerDelay,steps1,steps2);
        
    }
}
void Fwd(int x)
{Serial.println("moving forward ");
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
void Bck(int x)
{Serial.println("moving backward");
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,HIGH);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,HIGH);
    delay(x);
    digitalWrite(motor1,LOW);
    digitalWrite(motor11,LOW);    
    digitalWrite(motor2,LOW);
    digitalWrite(motor22,LOW);
}
void Rt(int x)
{Serial.println("moving right");
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
{Serial.println("moving left");
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
int motor1=12;
int motor11=11;
int motor2=10;
int motor22=9;
String action;
char direction1,direction2;
int recievedmsg1,recievedmsg2,recievedmsg3,recievedmsg4,recievedmsg5,recievedmsg6;
int concat_init_1,concat_init_2,FinalStep_1,FinalStep_2=0;

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

//***************main*****************//

void setup()
{
    pinMode(motor1,OUTPUT);
    pinMode(motor11,OUTPUT);
    pinMode(motor2,OUTPUT);
    pinMode(motor22,OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    Rt(100,200);
    action=Serial.readString();
    action.trim();

    direction1=action[0];//Dir1
    recievedmsg1=action[1]-48;
    recievedmsg2=action[2]-48;
    recievedmsg3=action[3]-48;
    direction2=action[4];//Dir2
    recievedmsg4=action[5]-48;
    recievedmsg5=action[6]-48;
    recievedmsg6=action[7]-48;

    concat_init_1=recievedmsg1*10+recievedmsg2;
    FinalStep_1=concat_init_1*10+recievedmsg3;//Step1

    concat_init_2=recievedmsg4*10+recievedmsg5;    
    FinalStep_2=concat_init_2*10+recievedmsg6;//Step2
    
}
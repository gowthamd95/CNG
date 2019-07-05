int pin_Out_S0 = 2;
int pin_Out_S1 = 3;
int pin_Out_S2 = 4;
int pin_In_Mux1 = A0;

int led = 12;

int pin_Out_S01 = 7;
int pin_Out_S11 = 8;
int pin_Out_S21 = 9;
int pin_In_Mux2 = A2;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin_Out_S0, OUTPUT);
  pinMode(pin_Out_S1, OUTPUT);
  pinMode(pin_Out_S2, OUTPUT);
  pinMode(pin_In_Mux1, INPUT);
    pinMode(pin_Out_S01, OUTPUT);
  pinMode(pin_Out_S11, OUTPUT);
  pinMode(pin_Out_S21, OUTPUT);
  pinMode(pin_In_Mux2, INPUT);
    pinMode(led, OUTPUT);
  
  Serial.begin(9600);
  
  
}

void loop() {
  analogWrite(led,255);
//delay(1000);
//analogWrite(led,LOW);
//delay(1000);
  // put your main code here, to run repeatedly:
  first();
  delay(1000);
 // second();

}
void first(){ 
  digitalWrite(pin_Out_S0,LOW);
  digitalWrite(pin_Out_S1,LOW);
  digitalWrite(pin_Out_S2,LOW);
  digitalWrite(pin_Out_S01,LOW);
  digitalWrite(pin_Out_S11,LOW);
  digitalWrite(pin_Out_S21,LOW);

 
  int pressure = analogRead(A0);
   //int gas = analogRead(A2);
   Serial.println("Pressure Sensor cylinder=");
   Serial.println(pressure);
   //Serial.println("Gas Sensor 1=");
   //Serial.println(gas);
   //delay(1000);
   //Serial.println("Pressure Sensor reducer=");
   //Serial.println(pressure);
   if(pressure > 2){
 digitalWrite(led,HIGH);
   }else{
digitalWrite(led,LOW);
}
}
//void second(){
//    digitalWrite(pin_Out_S0,LOW);
//  digitalWrite(pin_Out_S1,LOW);
//  digitalWrite(pin_Out_S2,HIGH);
//  digitalWrite(pin_Out_S01,LOW);
//  digitalWrite(pin_Out_S11,LOW);
//  digitalWrite(pin_Out_S21,HIGH);
//   int pressure1 = analogRead(A0);
//   int gas1 = analogRead(A2);
//  // Serial.println("Pressure Sensor reducer=");
////   Serial.println(pressure);
//   Serial.println("Gas Sensor 2=");
//   Serial.println(gas1);
//   delay(1000);
//   //digitalWrite(led,LOW);
//}

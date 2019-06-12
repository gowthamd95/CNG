int analoginpin1 = A0;
int analoginpin2 = A1;
int analoginpin3 = A2;

int sensorvalue1 = 0;
int sensorvalue2 = 0;
int sensorvalue3 = 0; 
String responseString = "";
int i = 0;
int j = 0;
int k = 0;

void setup() {
Serial.begin(9600);              //Starting serial communication
 
}
  
void loop() {
  i = analogRead(analoginpin1);
  j = analogRead(analoginpin2);
  k = analogRead(analoginpin3);
  responseString = "";
 //i = i + 10;
 //j = j + 20;
 //k = k + 30;
 responseString += i;
 responseString += "-";
 responseString += j;
 responseString += "*";
 responseString += k;
 responseString += "#";
 //Serial.write(i + "-" + j + "-" + k);
 writeString(responseString);
 delay(1000);
}
void writeString(String stringData) { // Used to serially push out a String with Serial.write()

  for (int i = 0; i < stringData.length(); i++)
  {
    Serial.write(stringData[i]);   // Push each char 1 by 1 on each loop pass
  }

}

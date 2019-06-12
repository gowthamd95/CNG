int analoginpin = A0;
int sensorvalue = 0; 
String responseString = "";
int i = 0;
int j = 0;
int k = 0;

void setup() {
Serial.begin(9600);              //Starting serial communication
 
}
  
void loop() {
  responseString = "";
 i = i + 10;
 j = j + 20;
 k = k + 30;
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

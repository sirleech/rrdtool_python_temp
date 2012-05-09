// Project Seven - temperature
//

int a;
int del=1000; // duration between temperature readings
float temperature;
int B=3975; 
float resistance;
int incomingByte; 

void setup()
{
  Serial.begin(38400);  
}

void loop()
{

  
    if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
        a=analogRead(0);
        resistance=(float)(1023-a)*10000/a; 
        temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;
        Serial.println(temperature);
    } 
  }
}


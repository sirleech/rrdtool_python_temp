// 10K Thermistor circuit hooked up to Analog 0
//

int a;
int del=1000; // duration between temperature readings
float temperature;
int B=3975; 
float resistance;

void setup()
{
  Serial.begin(38400);  
}

void loop()
{
  a=analogRead(0);
  resistance=(float)(1023-a)*10000/a; 
  temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;
  delay(del);
  Serial.println(temperature);
}


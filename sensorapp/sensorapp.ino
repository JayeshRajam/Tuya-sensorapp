const int Pin = 32; // the pin that the Moisture Sensor is attached to
int per;
int val=1024; 

void setup() {
  // initialize serial communication:
  Serial.begin(115200);
}

void loop() {
    val = analogRead(Pin);
    per = (-0.0477326968974*val) + 195.46539379; //linear conversion to percentage
    //Serial.println(per);
    if (Serial.available() > 0)
    {
    Serial.write(per);
    } 
    delay(100);
  }

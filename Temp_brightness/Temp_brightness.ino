String str = ",";
const int LDR = A0;
int input_val = 0;
#include <DHT.h> // Code for temp sensor is credited to Jacob Smith of the MakerLab!

DHT dht(3,DHT11);

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);

dht.begin();


}

void loop() {
  // put your main code here, to run repeatedly:

 
//  Serial.println("Brightness");
//  Serial.println(input_val);

  input_val = analogRead(LDR);  
  float humidity = dht.readHumidity();

   // Read temperature as Fahrenheit (isFahrenheit = true)
  float temp = dht.readTemperature(true);

  //display data
//  Serial.println("Humidity , Temperature");
  
  Serial.println(input_val + String(",") + temp + String(",") + humidity);


  //wait x milliseconds so printout it slower
  delay(1000);

}

// Special thanks to Jacob Smith of the makerlab for giving us a temperature sensor! This project wouldn't have been made without it. 

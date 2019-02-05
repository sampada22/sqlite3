#include "DHT.h"
#include <LiquidCrystal.h>

#define DHTPIN 2    //arduino pin connected to DHT11 sensor
const int rs = 3, en = 4, d4 = 5, d5 = 6, d6 = 7, d7 = 8;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

#define DHTTYPE DHT11   // DHT 11


DHT dht(DHTPIN, DHTTYPE);

struct sensor_Data
{
  int hum =0 ;
  int temp_in_C  = 0;
  int temp_in_F  = 0;
  int heatIndex_in_C = 0;
  int heatIndex_in_F = 0;
};  

sensor_Data sensor_Value;

void get_DHT_Values(void)
{
  sensor_Value.hum = dht.readHumidity();
  
  sensor_Value.temp_in_C = dht.readTemperature();
  sensor_Value.temp_in_F = dht.readTemperature(true);
  // Check if any reads failed and exit early (to try again).
  if (isnan(sensor_Value.hum) || isnan(sensor_Value.temp_in_C) || isnan(sensor_Value.temp_in_F)) {
    //Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  sensor_Value.heatIndex_in_F = dht.computeHeatIndex(sensor_Value.temp_in_F, sensor_Value.hum);
 
  // Compute heat index in Celsius (isFahreheit = false)
  sensor_Value.heatIndex_in_C = dht.computeHeatIndex(sensor_Value.temp_in_C,sensor_Value.hum, false);
 
}

void send_Sensor_Values(void)
{
  Serial.write('S');
  Serial.write((uint8_t *)&sensor_Value,sizeof(sensor_Value));
  Serial.write('E');
    return;
}

void showdataReceived()
{
  lcd.setCursor(0, 0);
  lcd.print("Hum:");
  lcd.print(sensor_Value.hum);
  lcd.print(", ");
  lcd.print("Temp:");
  lcd.print(sensor_Value.temp_in_C);

  lcd.setCursor(0, 1);
  lcd.print("HeatIndex:");
  lcd.print(sensor_Value.heatIndex_in_C);
  
}
void setup() {
  Serial.begin(9600);
  //Serial.println(F("DHTxx test!"));
  
  lcd.begin(16, 2);
  dht.begin();
}

void loop()
{
  delay(1000);
  //Serial.println("Arduino");
  get_DHT_Values();
//  Serial.print("Size of sensor values: %d",sizeof(sensor_Value));
  showdataReceived();
  send_Sensor_Values();
}




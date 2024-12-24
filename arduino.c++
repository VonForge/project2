#ВООБЩЕ ЭТО АРДУИНО, А НЕ С++
#define PIN_LED 10 
#define PIN_PHOTO_SENSOR A0 
#include <TroykaDHT.h> 
constexpr auto pinSensor = A4; 
DHT dht(2, DHT11); 
 
 
void setup() { 
  Serial.begin(9600); 
  pinMode(PIN_LED, OUTPUT); 
 
  Serial.begin(9600); 
  dht.begin(); 
} 
 
void loop() { 
  int val = analogRead(PIN_PHOTO_SENSOR); 
  Serial.println(val); 
  if (val < 985) { 
    digitalWrite(PIN_LED, LOW); 
  } else { 
    digitalWrite(PIN_LED, HIGH); 
  } 
 
 
  dht.read(); 
  // проверяем состояние данных 
  switch(dht.getState()) { 
    // всё OK 
    case DHT_OK: 
      // выводим показания влажности и температуры 
      Serial.print("Temperature = "); 
      Serial.print(dht.getTemperatureC()); 
      Serial.println(" C \t"); 
      Serial.print("Humidity = "); 
      Serial.print(dht.getHumidity()); 
      Serial.println(" %"); 
      break; 
    // ошибка контрольной суммы 
    case DHT_ERROR_CHECKSUM: 
      Serial.println("Checksum error"); 
      break; 
    // превышение времени ожидания 
    case DHT_ERROR_TIMEOUT: 
      Serial.println("Time out error"); 
      break; 
    // данных нет, датчик не реагирует или отсутствует 
    case DHT_ERROR_NO_REPLY: 
      Serial.println("Sensor not connected"); 
      break; 
  } 
  
  // ждём две секунды 
  delay(2000); 
 
 
 
  // считываем данные с датчика влажности почвы 
  int valueSensor = analogRead(pinSensor); 
  // выводим данные в Serial-порт 
  Serial.println(valueSensor); 
  // ждём 100 мс 
  delay(100); 
} 
/*// библиотека для работы с датчиками серии DHT 
 
// создаём объект класса DHT 
// передаём номер пина к которому подключён датчик и тип датчика 
// типы сенсоров: DHT11, DHT21, DHT22 
  
void setup() 
{ 
  // открываем последовательный порт для мониторинга действий в программе 
  Serial.begin(9600); 
  dht.begin(); 
} 
  
void loop() 
{ 
  // считывание данных с датчика 
  dht.read(); 
  // проверяем состояние данных 
  switch(dht.getState()) { 
    // всё OK 
    case DHT_OK: 
      // выводим показания влажности и температуры 
      Serial.print("Temperature = "); 
      Serial.print(dht.getTemperatureC()); 
      Serial.println(" C \t"); 
      Serial.print("Temperature = "); 
      Serial.print(dht.getTemperatureK()); 
      Serial.println(" K \t"); 
      Serial.print("Temperature = "); 
      Serial.print(dht.getTemperatureF()); 
      Serial.println(" F \t"); 
      Serial.print("Humidity = "); 
      Serial.print(dht.getHumidity()); 
      Serial.println(" %"); 
      break; 
    // ошибка контрольной суммы 
    case DHT_ERROR_CHECKSUM: 
      Serial.println("Checksum error"); 
      break; 
    // превышение времени ожидания 
    case DHT_ERROR_TIMEOUT: 
      Serial.println("Time out error"); 
      break; 
    // данных нет, датчик не реагирует или отсутствует 
    case DHT_ERROR_NO_REPLY: 
      Serial.println("Sensor not connected"); 
      break; 
  } 
  
  // ждём две секунды 
  delay(2000); 
} 
 
 
 
// любой GPIO пин с поддержкой АЦП 
  
void loop() { 
  // считываем данные с датчика влажности почвы 
  int valueSensor = analogRead(pinSensor); 
  // выводим данные в Serial-порт 
  Serial.println(valueSensor); 
  // ждём 100 мс 
  delay(100); 
} 
*/


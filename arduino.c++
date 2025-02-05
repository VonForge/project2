#define PIN_LED 10
#define PIN_PHOTO_SENSOR A0
#include <TroykaDHT.h>
#include <SPI.h>
constexpr auto pinSensor = A4;
DHT dht(4, DHT11);


void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}

int nam=12;
int Temperature=0;
int Humidity=0;

void loop() {
  // считываем данные с датчика влажности почвы
  int Soil = analogRead(pinSensor);
  // выводим данные в Serial-порт
  // ждём 100 мс
  


  int Light = analogRead(PIN_PHOTO_SENSOR);
  if (Light < 550) {
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
      Temperature=dht.getTemperatureC();
      Humidity=dht.getHumidity();
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
 
  Serial.print("\"N\":");
  Serial.print(nam);
  Serial.print(",\"Temperature\":");
  Serial.print(Temperature);
  Serial.print(",\"Humidity\":");
  Serial.print(Humidity);
  Serial.print(",\"Soil\":");
  Serial.print(Soil);
  Serial.print(",\"Light\":");
  Serial.println(Light);
  //Serial.println("\"N\":<{nam}>,\"Temperature\":<...>,\"Humidity\":<...>,\"Soil\":<...>,\"Light\":<...>");
  delay(1900);
}

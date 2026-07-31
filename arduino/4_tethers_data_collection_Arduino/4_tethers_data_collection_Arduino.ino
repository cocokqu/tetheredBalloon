#include <Adafruit_NAU7802.h>
#include <Wire.h>

// I2C address of TCA9548A multiplexer
const int TCA_ADDR = 0x70;

// TCA channels for each NAU7802
const int TETHER1_CH = 0;
const int TETHER2_CH = 1;
const int TETHER3_CH = 2;
const int TETHER4_CH = 3;

// DRDY pins, optional for now
const int DRDY1 = 10;
const int DRDY2 = 11;
const int DRDY3 = 12;
const int DRDY4 = 13;

// creating objects
Adafruit_NAU7802 tether1;
Adafruit_NAU7802 tether2;
Adafruit_NAU7802 tether3;
Adafruit_NAU7802 tether4;

// function to select one channel on the TCA multiplexer
void tcaSelect(uint8_t channel) {
  if (channel > 7) return;

  Wire.beginTransmission(TCA_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

void setup() {
  Serial.begin(115200);
  //dealy(1000);

  // start I2C
  Wire.begin();

  // optional for now
  pinMode(DRDY1, INPUT);
  pinMode(DRDY2, INPUT);
  pinMode(DRDY3, INPUT);
  pinMode(DRDY4, INPUT);

  // initialize tether 1
  tcaSelect(TETHER1_CH);
  if (!tether1.begin()) {
    Serial.println("Failed to find NAU7802 for tether 1");
    while (1);
  }

  // initialize tether 2
  tcaSelect(TETHER2_CH);
  if (!tether2.begin()) {
    Serial.println("Failed to find NAU7802 for tether 2");
    while (1);
  }

  // initialize tether 3
  tcaSelect(TETHER3_CH);
  if (!tether3.begin()) {
    Serial.println("Failed to find NAU7802 for tether 3");
    while (1);
  }

  // initialize tether 4
  tcaSelect(TETHER4_CH);
  if (!tether4.begin()) {
    Serial.println("Failed to find NAU7802 for tether 4");
    while (1);
  }

  Serial.println("time,tether1,tether2,tether3,tether4");
}

void loop() {
  Serial.print(millis());
  Serial.print(",");

  tcaSelect(TETHER1_CH);
  while (!tether1.available()) {
    delay(1);
  }
  Serial.print(tether1.read());
  Serial.print(",");

  tcaSelect(TETHER2_CH);
  while (!tether2.available()) {
    delay(1);
  }
  Serial.print(tether2.read());
  Serial.print(",");

  tcaSelect(TETHER3_CH);
  while (!tether3.available()) {
    delay(1);
  }
  Serial.print(tether3.read());
  Serial.print(",");

  tcaSelect(TETHER4_CH);
  while (!tether4.available()) {
    delay(1);
  }
  Serial.print(tether4.read());

  Serial.println();

  delay(100);
}
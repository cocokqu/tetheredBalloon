#include <Adafruit_NAU7802.h>
#include <Wire.h>

// I2C address of TCA9548A multiplexer
const int TCA_ADDR = 0x70;

// TCA channel for the tether 
const int TETHER_CH = 0;

// Create NAU7802 object
Adafruit_NAU7802 tether;

// Select one channel on the TCA9548A multiplexer
void tcaSelect(uint8_t channel) {
  if (channel > 7) return;

  Wire.beginTransmission(TCA_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

void setup() {
  Serial.begin(115200);
  //why delay
  delay(1000);

  // start I2C
  Wire.begin();

  // Select the multiplexer channel for tether 1
  tcaSelect(TETHER_CH);

  // Start NAU7802
  if (!tether.begin()) {
    Serial.println("Failed to find NAU7802 for tether");
    while (1);
  }

  Serial.println("Found NAU7802");

  // // Optional but useful setup
  // tether.setLDO(NAU7802_3V0);
  // tether.setGain(NAU7802_GAIN_128);
  // tether.setRate(NAU7802_RATE_10SPS);

  // Wait for sensor to settle
  delay(1000);

  // Print CSV header
  Serial.println("time_ms,raw1");
}

void loop() {
  tcaSelect(TETHER_CH);

  while (!tether.available()) {
    delay(1);
  }

  int32_t raw = tether.read();

  Serial.print(millis());
  Serial.print(",");
  Serial.println(raw);

  delay(100);
}
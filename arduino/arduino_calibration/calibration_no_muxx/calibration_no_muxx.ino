#include <Adafruit_NAU7802.h>
#include <Wire.h>

// Create NAU7802 object
Adafruit_NAU7802 tether;

// Averaging parameters
const unsigned long AVERAGE_TIME_MS = 10000; // 10 seconds

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Start I2C
  Wire.begin();

  // Start NAU7802
  if (!tether.begin()) {
    Serial.println("Failed to find NAU7802");
    while (1);
  }

  Serial.println("Found NAU7802");

  // Optional configuration
  // tether.setLDO(NAU7802_3V0);
  // tether.setGain(NAU7802_GAIN_128);
  // tether.setRate(NAU7802_RATE_10SPS);

  delay(1000);

  Serial.println("Averaging readings over 10 seconds...");
  Serial.println("time_ms,average_raw");
}

void loop() {
  long long sum = 0;          // Prevent overflow
  uint32_t count = 0;

  unsigned long startTime = millis();

  while (millis() - startTime < AVERAGE_TIME_MS) {

    if (tether.available()) {
      sum += tether.read();
      count++;
    }
  }

  float average = 0;
  if (count > 0) {
    average = (float)sum / count;
  }

  Serial.print(millis());
  Serial.print(",");
  Serial.println(average, 2);
}
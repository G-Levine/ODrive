#include <AS5048A.h>

// Uses this library: https://github.com/ZoetropeLabs/AS5048A-Arduino

#define INTERVAL            125

AS5048A angleSensor(10);

void setup()
{
	Serial.begin(19200);
	angleSensor.init();
}

void loop()
{
  int curr_us;
  int last_us = micros();

  do {
    curr_us = micros();
  } while (curr_us - last_us < INTERVAL);
  
	word val = angleSensor.getRawRotation();
	Serial.println(val, DEC);
}

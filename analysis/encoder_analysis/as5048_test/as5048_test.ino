#include <AS5048A.h>

// Uses this library: https://github.com/ZoetropeLabs/AS5048A-Arduino


AS5048A angleSensor(10);

void setup()
{
	Serial.begin(19200);
	angleSensor.init();
}

void loop()
{
	delay(0.125);

	word val = angleSensor.getRawRotation();
	Serial.println(val, DEC);
}

#include <MagAlpha.h>

// Uses this library: https://github.com/monolithicpower/MagAlpha-Arduino-Library


//Check https://www.arduino.cc/en/reference/SPI for SPI signals connections

#define UART_BAUDRATE       115200        //UART data rate in bits per second (baud)
#define SPI_SCLK_FREQUENCY  10000000      //SPI SCLK Clock frequency in Hz
#define SPI_CS_PIN          10             //SPI CS pin
#define INTERVAL            125

MagAlpha magAlpha;

void setup() {
  // put your setup code here, to run once:
  //Set the SPI SCLK frequency, SPI Mode and CS pin
  magAlpha.begin(SPI_SCLK_FREQUENCY, MA_SPI_MODE_3, SPI_CS_PIN);
  //Set the Serial Communication used to report the angle
  Serial.begin(UART_BAUDRATE);

}

void loop() {
    double angle;
    int curr_us;
    int last_us = micros();

    do {
      curr_us = micros();
    } while (curr_us - last_us < INTERVAL);
    
    //Read the angle
    angle = magAlpha.readAngleRaw16() / 4; // Convert to 14-bit
    Serial.println(angle, 3);
}

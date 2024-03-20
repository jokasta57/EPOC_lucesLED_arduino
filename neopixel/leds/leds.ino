/*
	Capitulo 29 de Arduino desde cero en Español.
	Programa que demuestra el funcionamiento de una tira de 8 Neopixel encadenados
	encendiendo cada uno de sus elementos en color azul. Requiere la instalacion
	de la libreria Adafruit Neopixel.

	Autor: bitwiseAr  

*/

#include <Adafruit_NeoPixel.h>  // importa libreria

// Primer parametro = cantidad de pixeles en la tira
// Segundo parametro = pin de conexion a Arduino
// Tercer parametro:
//   NEO_KHZ800  800 KHz velocidad de datos (WS2812 y nuevos)
//   NEO_KHZ400  400 KHz velocidad de datos (WS2811 y mas antiguos)
//   NEO_GRB     flujo de datos en orden GRB (WS2812 y nuevos)
//   NEO_RGB     flujo de datos en orden RGB (versiones mas antiguas)

Adafruit_NeoPixel tira = Adafruit_NeoPixel(300, 2, NEO_GRB + NEO_KHZ800);  // creacion de objeto "tira"
// con una cantidad de 8 pixeles, sobre pin 2 de Arduino y configurado para WS2812




String strs[5];
int StringCount = 0;
String SerialData;


void setup() {

  Serial.begin(9600);

  tira.begin();  // inicializacion de la tira

  tira.setBrightness(250);

  tira.clear();  // restablece todos los pixeles en apagado
}


void loop() {

  while (Serial.available() > 0) {

    SerialData = Serial.readStringUntil('.');

    // Split the string into substrings
    while (SerialData.length() > 0) {

      int index = SerialData.indexOf(' ');

      if (index == -1)  // No space found
      {
        strs[StringCount++] = SerialData;
        break;

      } else {

        strs[StringCount++] = SerialData.substring(0, index);

        SerialData = SerialData.substring(index + 1);
      }
    }


    if (strs[0] == "beta") {
      
      configuraciones_leds(strs[0], strs[1]);
      //snowflakes(1000);
      //rainbowCycle(20);

    } else if (strs[0] == "alpha") {

      configuraciones_leds(strs[0], strs[1]);
      //snowflakes(100000);
    }
  }
}


void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for (j = 0; j < 256 * 5; j++) {  // 5 cycles of all colors on wheel
    for (i = 0; i < tira.numPixels(); i++) {
      tira.setPixelColor(i, Wheel(((i * 256 / tira.numPixels()) + j) & 255));
    }
    tira.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if (WheelPos < 85) {
    return tira.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if (WheelPos < 170) {
    WheelPos -= 85;
    return tira.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return tira.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

void snowflakes(uint8_t wait) {

  // Setup the pixel array
  int pixel[300];
  for (int p = 0; p < 60; p++) {
    pixel[p] = random(0, 255);
  }

  // Run some snowflake cycles
  for (int j = 0; j < 200; j++) {

    // Every five cycles, light a new pixel
    if ((j % 5) == 0) {
      tira.setPixelColor(random(0, 60), 255, 255, 255);
    }

    // Dim all pixels by 10
    for (int p = 0; p < 300; p++) {
      tira.setPixelColor(p, pixel[p], pixel[p], pixel[p]);
      pixel[p] = pixel[p] - 10;
    }
    tira.show();
    delay(wait);
  }
}


void configuraciones_leds(String eeg, String hz) {

  //////////////// EEG + TIRA "1" //////////////

  if (eeg == "alpha") {

    //Asignando brillo, dependiendo de Hz de EEG
    switch (round(hz.toFloat())) {
      case 8:
        tira.setBrightness(50);
        break;
      case 9:
        tira.setBrightness(100);
        break;
      case 10:
        tira.setBrightness(150);
        break;
      case 11:
        tira.setBrightness(200);
        break;
      case 12:
        tira.setBrightness(250);
        break;
      default:
        tira.setBrightness(50);
        break;
    }



    //Definicion de bloques de colores
    for (int i = 0; i < 25; i++) {  //#F39C12

      tira.setPixelColor(i, 243, 156, 18);
    }

    for (int i = 25; i < 100; i++) {  //#D35400

      tira.setPixelColor(i, 211, 84, 0);
    }

    for (int i = 100; i < 200; i++) {  //#BA4A00

      tira.setPixelColor(i, 186, 74, 0);
    }

    for (int i = 200; i < 275; i++) {  //#D35400

      tira.setPixelColor(i, 211, 84, 0);
    }

    for (int i = 275; i < 300; i++) {  //#E59866

      tira.setPixelColor(i, 47, 6, 45);
    }




  } else if (eeg == "beta") {

    //Asignando brillo, dependiendo de Hz de EEG
    switch (round(strs[1].toFloat())) {
      case 12:
        tira.setBrightness(50);
        break;
      case 13:
        tira.setBrightness(61);
        break;
      case 14:
        tira.setBrightness(72);
        break;
      case 15:
        tira.setBrightness(83);
        break;
      case 16:
        tira.setBrightness(94);
        break;
      case 17:
        tira.setBrightness(105);
        break;
      case 18:
        tira.setBrightness(116);
        break;
      case 19:
        tira.setBrightness(127);
        break;
      case 20:
        tira.setBrightness(138);
        break;
      case 21:
        tira.setBrightness(149);
        break;
      case 22:
        tira.setBrightness(160);
        break;
      case 23:
        tira.setBrightness(171);
        break;
      case 24:
        tira.setBrightness(182);
        break;
      case 25:
        tira.setBrightness(193);
        break;
      case 26:
        tira.setBrightness(204);
        break;
      case 27:
        tira.setBrightness(215);
        break;
      case 28:
        tira.setBrightness(226);
        break;
      case 29:
        tira.setBrightness(237);
        break;
      case 30:
        tira.setBrightness(250);
        break;
      default:
        tira.setBrightness(10);
        break;
    }


    //Definicion de bloques de colores
    for (int i = 0; i < 25; i++) {  //#48C9B0
      tira.setPixelColor(i, 72, 201, 176);
    }

    for (int i = 25; i < 100; i++) {  //#138075
      tira.setPixelColor(i, 19, 128, 117);
    }

    for (int i = 100; i < 200; i++) {  //#117864
      tira.setPixelColor(i, 17, 120, 100);
    }

    for (int i = 200; i < 275; i++) {  //#138D75
      tira.setPixelColor(i, 19, 141, 117);
    }

    for (int i = 275; i < 299; i++) {  //#A3E4D7
      tira.setPixelColor(i, 163, 228, 215);
    }


  } else if (eeg == "") {  // si viene vacío

    for (int i = 1; i < 300; i++) {  //rojo

      tira.setPixelColor(i, 255, 0, 0);
    }
  }

  tira.show();  // <----- siempre va afuera de las condicionales, para que pueda hacer los cambios en los LEDs!
}

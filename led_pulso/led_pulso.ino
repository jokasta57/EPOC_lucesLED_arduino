

#include <Adafruit_NeoPixel.h>  // importa libreria

// Primer parametro = cantidad de pixeles en la tira
// Segundo parametro = pin de conexion a Arduino
// Tercer parametro:
//   NEO_KHZ800  800 KHz velocidad de datos (WS2812 y nuevos)
//   NEO_KHZ400  400 KHz velocidad de datos (WS2811 y mas antiguos)
//   NEO_GRB     flujo de datos en orden GRB (WS2812 y nuevos)
//   NEO_RGB     flujo de datos en orden RGB (versiones mas antiguas)

// con una cantidad de 8 pixeles, sobre pin 2 de Arduino y configurado para WS2812

Adafruit_NeoPixel tira = Adafruit_NeoPixel(300, 2, NEO_GRB + NEO_KHZ800);  // creacion de objeto "tira"



//String strs[5];
//int StringCount = 0;
//String SerialData;


void setup() {

  Serial.begin(9600);

  tira.begin();  // inicializacion de la tira

  tira.setBrightness(255);

  tira.show();
}


void loop() {

  while (Serial.available() > 0) {

    String bpm = Serial.readStringUntil('.');

    on_off_cycle(bpm.toFloat());  //esto debe comentarse, ya que solo sirve de prueba
  }

  //String bpm = "100";
  //on_off_cycle(bpm.toFloat());  //esto debe comentarse, ya que solo sirve de prueba
}

void on_off_cycle(float pulse) {

  //Serial.println(pulse);

  if (pulse == 0) {  // si viene vacío

    for (int i = 1; i < 300; i++) {  //rojo

      tira.setPixelColor(i, 255, 0, 0);
    }
  } else {

    //Definicion de bloques de colores
    for (int i = 0; i < 150; i++) {  //#F1C40F
      tira.setPixelColor(i, 47, 12, 6);
    }

    for (int i = 150; i < 300; i++) {  //#F7DC6F
      tira.setPixelColor(i, 247, 220, 111);
    }
  }

  tira.show();  // Mostrar los cambios en la tira de neopíxeles


  // Asegurarse de que el pulso esté en el rango válido (0-255)
  pulse = constrain(pulse, 0, 255);

  pulse = 6000 / pulse;

  for (int i = 0; i < 3; i++) {

    if (i % 2 == 0) {

      tira.show();  //Colocar esta instrucción para mostrar el color

    } else {

      tira.clear();  // restablece todos los pixeles en apagado
    }

    delay(pulse);
  }
}

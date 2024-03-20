EEG_ Emotiv - App desde python.
Convirtiendo las señales EEG en luces LED, con arduino.

1.- crear cuenta

![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/3e24ebb1-bca1-46a3-a4b9-ab213e543a0b)

Hay que llenar un cuestionario al iniciar a desarrollar tu propia App.

2.- IMPORTANTE: Agregar tu client_ID y client_secret a tu script 

![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/8f552a8d-5a39-435b-8a7f-ddefa9c7896f)


3.-Ejecutar EMOTIV Launcher!

![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/1f7bd41e-282c-4fd7-a5fc-7aaf894755b3)


4.- Requerimientos/instalar

#This example works with Python >= 3.7
Install websocket client via pip install websocket-client
Install python-dispatch via pip install python-dispatch



5.- Comprar la licencia, para obtener los RAW data de la EEG, o solo trabajamos con en Band power

![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/156ce458-044f-4cfb-b508-7ade927f035d)

Explicación de las etiquetas.

https://emotiv.gitbook.io/cortex-api/data-subscription/data-sample-object
![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/30e08254-537f-4bb3-865a-ca7ec726bb0d)


6.- COMUNICACIÓN Python + Arduino!

Se usó la tira LED Neopixel: 
NEOPIXEL (luces LED) + Arduino: 
https://www.youtube.com/watch?v=OB__BBa4Ob8&feature=youtu.be
![image](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/371a2185-1db7-4b30-b69a-131d246a45a9)


#Tutorial: https://www.youtube.com/watch?v=fCuFDW1RoxI&ab_channel=JulianRuiz

pip install pyserial  


Del mismo modo, se transformó el pulso sanguíneo, en combinación de colores, a través de este sensor, y esta la forma de conectarlo al arduino:
![Wiring-Connecting-Pulse-Sensor-with-Arduino](https://github.com/jokasta57/EPOC_lucesLED_arduino/assets/16157859/52c218ea-b5bc-4047-be7e-d102b2a26fbe)


7.- Finalmente, ejecutar estos pasos:


Entrar al directorio donde se encuentre todo el proyecto, y ejecutar:
python sub_data.py

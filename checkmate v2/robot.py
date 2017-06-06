from time import sleep
import RPi.GPIO as GPIO

#El retraso que tendra el cambio de pasos en segundos
d = .002;
#numero de pasos en todo el tablero
pasosTotales = 6250;

#cuantos pasos debe de hacer el motor para recorrer un cuadrito del tablero
pasosPorCuadro = pasosTotales//8;

#éstos pines son del motor de las X
motorX=[4,5,6,7];

#estos pines son del motor de las Y 
motorY=[8,9,10,11];

#Igualamos funciones y constantes que se utilizan en arduino
OUTPUT = GPIO.OUT
INPUT = GPIO.IN
LOW = False
HIGH = True
digitalWrite = GPIO.output
pinMode = GPIO.setup

#mueve el motor hacia adelante los cuadritos que le digas
#tu pones cual motor quieres que se mueva mediante los pines
def avanza(x, pines):
	muevePasosDelante(pasosPorCuadro*x,pines);

#gira en reversa el motor que le digas, los cuadritos que le digas
def retrocede(x, pines):
	muevePasosReversa(pasosPorCuadro*x,pines);

#mueve el motor que le digas, mediante los pines, la cantidad de pasos que le digas, hacia adelante 
def muevePasosDelante (pasos, pines):

	pinMode(pines[0], OUTPUT);
	pinMode(pines[1], OUTPUT);
	pinMode(pines[2], OUTPUT);
	pinMode(pines[3], OUTPUT); 
	
	digitalWrite(pines[0], LOW);
	digitalWrite(pines[1], LOW);
	digitalWrite(pines[2], LOW);
	digitalWrite(pines[3], LOW);  
	
	for i in range(pasos):
    
		digitalWrite(pines[0], HIGH);
		digitalWrite(pines[1], LOW);
		digitalWrite(pines[2], HIGH);
		digitalWrite(pines[3], LOW);
		sleep(d);
		digitalWrite(pines[0], HIGH);
		digitalWrite(pines[1], LOW);
		digitalWrite(pines[2], LOW);
		digitalWrite(pines[3], HIGH);
		sleep(d);
		digitalWrite(pines[0], LOW);
		digitalWrite(pines[1], HIGH);
		digitalWrite(pines[2], LOW);
		digitalWrite(pines[3], HIGH);
		sleep(d);
		digitalWrite(pines[0], LOW);
		digitalWrite(pines[1], HIGH);
		digitalWrite(pines[2], HIGH);
		digitalWrite(pines[3], LOW);
		sleep(d);}

#mueve el motor que le digas mediante los pines, la cantidad de pasos que va a hacer girando en reversa.
def muevePasosReversa (pasos, pines):

	pinMode(pines[0], OUTPUT);
	pinMode(pines[1], OUTPUT);
	pinMode(pines[2], OUTPUT);
	pinMode(pines[3], OUTPUT); 
    
	digitalWrite(pines[0], LOW);
	digitalWrite(pines[1], LOW);
	digitalWrite(pines[2], LOW);
	digitalWrite(pines[3], LOW);  
	
	for i in range(pasos):
 
    
		digitalWrite(pines[0], LOW);
		digitalWrite(pines[1], HIGH);
		digitalWrite(pines[2], HIGH);
		digitalWrite(pines[3], LOW);
		sleep(d);
		digitalWrite(pines[0], LOW);
		digitalWrite(pines[1], HIGH);
		digitalWrite(pines[2], LOW);
		digitalWrite(pines[3], HIGH);
		sleep(d);
		digitalWrite(pines[0], HIGH);
		digitalWrite(pines[1], LOW);
		digitalWrite(pines[2], LOW);
		digitalWrite(pines[3], HIGH);
		sleep(d);
		digitalWrite(pines[0], HIGH);
		digitalWrite(pines[1], LOW);
		digitalWrite(pines[2], HIGH);
		digitalWrite(pines[3], LOW);
		sleep(d);
		
#ingresa tu posicion actual y a donde quieres ir
def posiciones(actual, destino)
	y= (actual[0] - destino[0]);
	x= (actual[1] - destino[1]);
    #si es un numero negativo, tiene que irse para atrás
    #si es igual a 0 no va a pasar absolutamente nada, no se movería ningún paso hacia ningun lado en ese eje.
    if(x > 0):
		retrocede(x,motorX);
       
    #si es un número positivo va hacia adelante
    elif(x<0):
		avanza(abs(x),motorX);

    if(y > 0):
		retrocede(y,motorY);
    elif (y< 0):
		avanza(abs(y),motorY);

if __name__ == '__main__': 
	pinMode(8,OUTPUT);
	pinMode(9,OUTPUT);
	pinMode(10,OUTPUT);
	pinMode(11,OUTPUT);
	pinMode(4,OUTPUT);
	pinMode(5,OUTPUT);
	pinMode(6,OUTPUT);
	pinMode(7,OUTPUT);
	
	
  	# muevePasosReversa(pasosTotales);
	# sleep(1000);
	# muevePasosDelante(pasosTotales);
	# sleep(1000);
	while True:
		x ={5,5}; 
		y ={8,8}; 
		#poner de donde a donde quieres ir
		posiciones(x,y);
	
	# Hacemos una limpieza de los GPIO
	GPIO.cleanup()

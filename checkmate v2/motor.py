from time import sleep
import RPi.GPIO as GPIO
import threading

#Igualamos funciones y constantes que se utilizan en arduino
OUTPUT = GPIO.OUT
INPUT = GPIO.IN
LOW = False
HIGH = True
digitalWrite = GPIO.output
pinMode = GPIO.setup

class CNC():
	def __init__(self, pinesX, pinesY):
#El retraso que tendra el cambio de pasos en segundos
	self.d = .002;
	#numero de pasos en todo el tablero
	self.pasosTotales = 6250;

	#cuantos pasos debe de hacer el motor para recorrer un cuadrito del tablero
	self.pasosPorCuadro = self.pasosTotales//8;

	#éstos pines son del motor de las X y Y
	self.motorX=pinesX;
	self.motorY=pinesY;
	
	self.avaibleX = True
	self.avaibleY = True
	

	#mueve el motor hacia adelante los cuadritos que le digas
	#tu pones cual motor quieres que se mueva mediante los pines
	def avanza(self, x, pines):
		self.muevePasosDelante(pasosPorCuadro*x,pines);

	#gira en reversa el motor que le digas, los cuadritos que le digas
	def retrocede(self, x, pines):
		self.muevePasosReversa(pasosPorCuadro*x,pines);

	#mueve el motor que le digas, mediante los pines, la cantidad de pasos que le digas, hacia adelante 
	def muevePasosDelante (self, pasos, pines):

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
	def muevePasosReversa (self, pasos, pines):

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
	
	def runMotor(self, motor, sentido, cuadros):
		if sentido:
			if motor == motorX:
				self.avaibleX = False
				self.avanza(cuadros,motor))
				self.avaibleX = True
			else:
				self.avaibleY = False
				self.avanza(cuadros,motor))
				self.avaibleY = True
		else:
			if motor == motorX:
				self.avaibleX = False
				self.retrocede(cuadros,motor))
				self.avaibleX = True
			else:
				self.avaibleY = False
				self.retrocede(cuadros,motor))
				self.avaibleY = True
				
				
	#ingresa tu posicion actual y a donde quieres ir
	def posiciones(self, actual, destino)
		y= (actual[0] - destino[0]);
		x= (actual[1] - destino[1]);
		#si es un numero negativo, tiene que irse para atrás
		#si es igual a 0 no va a pasar absolutamente nada, no se movería ningún paso hacia ningun lado en ese eje.
		threads = list()
		if(x >= 0):
			runX = threading.Thread(target=self.runMotor(self.motorX, True, x))
		else:
			runX = threading.Thread(target=self.runMotor(self.motorX, False, x))
			
		if(y >= 0):
			runY = threading.Thread(target=self.runMotor(self.motorX, True, x))
		else:
			runY = threading.Thread(target=self.runMotor(self.motorX, False, x))
		
		threads.append(runX)
		threads.append(runY)
		
		
		while True:
			if self.avaibleX and self.avaibleY:
				runX.start()
				runY.start()
				break


if __name__ == '__main__':	
  	# muevePasosReversa(pasosTotales);
	# sleep(1000);
	# muevePasosDelante(pasosTotales);
	# sleep(1000);
	m = motor([17, 18, 19, 20])
		#poner de donde a donde quieres ir
	m.posiciones(x,y);
	
	# Hacemos una limpieza de los GPIO
	GPIO.cleanup()

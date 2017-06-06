#!/usr/bin/env python
from PDI import *
from webcam import *
from alphabeta import chessAI
import threading
import time
import chess

size = (600,600)

class player:
	def __init__(self, color, board):
		self.color = color
		if self.color:
			self.playerType = int(input("White is a: \n1) Human \nother) AI\n"))
		else:
			self.playerType = int(input("Black is a: \n1) Human \nother) AI\n"))
		
		if self.playerType == 1:
			self.boardImg = boardImg(board)
		else:
			self.AI = chessAI(int(input("Lvl de AI (Entero): ")),self.color)
			
	def move(self, board):
		if self.playerType == 1: #Si es humano
			self.moveHuman(board)
		else:
			self.moveAI(board)
			
	def moveHuman(self, board):
		#self.boardImg.viewBoard()
		while(True):
			time.sleep(1)
			self.boardImg.updateBoard(webcam.frame)
			for m in board.legal_moves:
				#Si se encuentra en el tablero que se movio esa pieza, se actualiza el tablero virtual
				if boardImg.readMove(m):
					print("El humano ha movido", m)
					board.push(m)
					break
			
			#Si ya es turno del oponente, sal del loop
			if board.turn != self.color:
				break
			
		
	def moveAI(self, board):
		board.push(self.AI.rootAI(board))
		
class game:
	def __init__(self, board = chess.Board()):
		self.board = board
		self.whitePlayer = player(True, self.board)
		self.blackPlayer = player(False, self.board)
			
	def startgame(self):
		
		#Revisa que no haya jaquemate, punto muerto, material insuficiente, 
		#regla del setentaycincoavo movimiento, quintupla repeticion,
		# o variantes de condicion final para continuar
		while not(self.board.is_game_over()):
			clear()
			print(self.board)
			if self.board.turn: #Si es turno de las blancas
				whitePlayer.move(self.board)
				
			else: #Si es turno de las negras
				blackPlayer.move(self.board)
				self.board.peek()
		
		print("El resultado es: " + self.board.result())
		
def boardView(boardImg):
	while True:
		img = boardImg.img
		cv2.imshow("boardView", img)
		k = cv2.waitKey(1)

		if k%256 == 27:
			# ESC pressed
			print("Escape hit, closing...")
			break

def testPDI():
	#Prueba de PDI
	board = chess.Board()
	img = cv2.imread("captures/board0.png")
	
	boardimg = boardImg(img, board)
	#boardimg.boardView()
	#boardimg.drawPieces()
	#boardimg.boardView()
	#cv2.imwrite("test2.jpg", boardImg.img)
	
	for m in board.legal_moves:
		
		if boardimg.readMove(str(m)):
			print("se realizo el movimiento ",m)
			board.push(m)
			break
	
	print(board)
	
def testWebCam():
	#Creamos un hilo en el que podemos ver lo que captura la cámara
	threads = list()
	cam = webcam()
	camView = threading.Thread(target=cam.webcamView)
	threads.append(camView)
	camView.start()
	time.sleep(2)
	return cam

if __name__ == '__main__':
	#boardImg = boardImg(img, board)
	testPDI()
	

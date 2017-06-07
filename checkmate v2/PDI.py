#!/usr/bin/env python
import numpy as np
import cv2
import argparse
import imutils
from webcam import webcam
import chess
import time
import threading


class pieceDetector:
	def __init__(self):
		pass

	def detect(self, c):
		piece = "unknown"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.06 * peri, True)

		if len(approx) == 3:
			piece = "p"

		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			piece = "b" if ar >= 0.95 and ar <= 1.05 else "n"

		elif len(approx) == 5:
			piece = "r"
		
		elif len(approx) == 6:
			piece = "q"
		
		else:
			piece = "k"
		
		return piece


class boardImg():
	def __init__(self, img=cv2.resize(cv2.imread("captures/board0.png"),(600,600)), board = chess.Board()):
		
		self.img = img
		self.recognizeBoard()
		self.size = self.img.shape[:2]
		self.board = board
		self.sd = pieceDetector()
		#self.drawSquares()
		
		
	def updateBoard(self, img):	
		self.img = img
		self.recognizeBoard()
		self.size = self.img.shape[:2]
		self.drawSquares()
		
	def drawShapes(self, shapes, img):
		cv2.drawContours( img, shapes, -1, (0, 255, 0), 3)
		cv2.imshow('squares', img)
		cv2.waitKey(0)

	def createSquare(self, start, l):
		#Esta funcion recibe las coordenadas del punto superior izquierdo de un cuadrado
		#y devuelve las coordenadas de los 4 puntos de un cuadrado en el tablero
		x = start[0]
		y = start[1]
		if x < 0:
			x = 0
		elif x + l > self.size[0]:
			x = self.size[0] - l
		if y < 0:
			y = 0	
		elif start[1] + l > self.size[1]:
			y = self.size[1] - l
		return np.array([[x, y], \
						[x, y + l], \
						[x + l, y + l], \
						[x + l, y]])
		

	def createCoordsBoard(self):
		l = int(self.size[0]/8)
		coords = []
		for j in range(8):
			for i in range(8):
				coords.append(self.createSquare([i*l, self.size[1] - j*l-l], l))
				
		return coords
	
	def detectPieces(self, img):
		# convierte la imagen redimensionada a escala de grises, se aplica blur y threshold
		resized = imutils.resize(img, width=300)
		ratio = img.shape[0] / float(resized.shape[0])
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
		
		# busca los contornos que tienen los valores del umbral
		contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
		#self.squareView(self.img)
		piece = []
		
		for cnt in contours[1]:
				cnt_len = cv2.arcLength(cnt, True)
				cont = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
				if cv2.contourArea(cont) > 100 and cv2.contourArea(cont) < 28000:
					piece.append(cnt)
		
		return piece

	def drawPieces(self):
		cnts = self.detectPieces(self.img)
		if len(cnts)==0:
			print("No hay piezas")
		sd = pieceDetector()
		for c in cnts:
			# calcula el centro de masa de la figura y define que figura es
			M = cv2.moments(c)
			if (M["m10"] > 0 and M["m00"] > 0 and M["m01"] > 0):
				cX = int((M["m10"] / M["m00"]))
				cY = int((M["m01"] / M["m00"]))+28
				piece = sd.detect(c)
				# multiply the contour (x, y)-coordinates by the resize ratio,
				# then draw the contours and the name of the shape on the image
				
				c = c.astype("int")
				cv2.drawContours(self.img, [c], -1, (0, 255, 0), 2)
				cv2.putText(self.img, piece, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
					0.5, (255, 255, 255), 2)
		
				
	def drawNamePieces(self, board):
		#Tipos de pieza PAWN = 1, KNIGHT = 2, BISHOP = 3, ROOK = 4, QUEEN = 5, KING = 6
		pieces = ["bPeon", "bCaballo", "bAlfil", "bTorre", "bDama", "bRey", "wPeon", "wCaballo", "wAlfil", "wTorre", "wDama", "wRey"]
		for turn in (0, 1):
			for i in range(1,7):
				for p in board.pieces(i,turn):
					cX = int((p)%8) * int(self.size[0]/8) + 20
					cY = int((p)/8) * int(self.size[1]/8) + int(self.size[1]/16)+30
					cv2.putText(self.img, pieces[turn * 6 + i-1], (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
						0.5, (255, 255, 255), 2)
						
	def readMove(self, m):
		#Devuelve true o false dependiendo de si se detecta el movimiento
		#Si no se encuentra pieza en el origen del movimiento legal, probablemente se realizo ese movimiento
		square = self.boardSquare((ord(m[0])-97,int(m[1])-1))
		#self.squareView(square)
		if len(self.detectPieces(square)) == 0:
			print("Cuadro vacio")
			#Si se encuentra la pieza en su posible destino, seguramente se realizo ese movimiento
			square = self.boardSquare((ord(m[2])-97,int(m[3])-1))
			#self.squareView(square)
			pieces = self.detectPieces(square)
			if len(pieces) == 1:
				print("Se encontro pieza")
				namePiece = self.sd.detect(pieces[0])
				#print(namePiece, str(self.board.piece_at(ord(m[0])-97+(int(m[1])-1)*8)).lower())
				if namePiece == str(self.board.piece_at(ord(m[0])-97+(int(m[1])-1)*8)).lower() or str(self.board.piece_at(ord(m[0])-97+(int(m[1])-1)*8)).lower() == 'k':
					return True
		return False		
		
	def boardSquare(self, coord):
		l = int(self.size[0]/8)
		square = self.createCoordsBoard()[coord[0]+coord[1]*8]
		return self.img[square[0][1]:square[2][1], square[0][0]:square[2][0]]
		
	def createBoardImgs(self):
		squares = self.createCoordsBoard()
		#Crea una matriz 8x8 de imágenes del tamaño de un cuadrado cada imagen
		squareOfBoard = np.vectorize(np.zeros((int(self.size[0]/8),int(self.size[1]/8))))
		boardImgs = np.empty((8,8), dtype=object)
		boardImgs[:,:] = squareOfBoard
		
		x = 0
		y = 0
		for square in squares:
			boardImgs[x][y] = self.img[square[0][1]:square[2][1], square[0][0]:square[2][0]]
			x += 1
			if x == 8:
				y += 1
				x = 0
		self.boardImgs = boardImgs
		return self.boardImgs

	def angle_cos(self, p0, p1, p2):
		d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
		return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
		
	def detectBoard(self):
		#Devuelve las coordenadas de los 4 puntos del cuadrado mas grande de la imagen
		#Que se considerará como el tablero
		img = cv2.GaussianBlur(self.img, (5, 5), 0)
		board = None
		#Solo usamos el canal verde para buscar el tablero
		R, G, B = cv2.split(img)
		gray = G
		for thrs in range(0, 255, 26):
			if thrs == 0:
				bin = cv2.Canny(gray, 0, 50, apertureSize=5)
				bin = cv2.dilate(bin, None)
			else:
				retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
			bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			for cnt in contours:
				cnt_len = cv2.arcLength(cnt, True)
				cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
				if len(cnt) == 4 and cv2.contourArea(cnt) > 5000 and cv2.isContourConvex(cnt):
					cnt = cnt.reshape(-1, 2)
					max_cos = np.max([self.angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
					if max_cos < 0.1:
						board = cnt
		
		return board

	def drawSquares(self):
		squares = self.createCoordsBoard()
		cv2.drawContours(self.img, squares, -1, (0, 255, 0), 3)
		
		
	def recognizeBoard(self):
		#Esta funcion encuentra el cuadrado más grande de la imagen y lo considera como el tablero, entonces devuelve la imagen del tablero
		boardCoords = self.detectBoard()
		bord = 4
		self.img = self.img[boardCoords[0][1]+bord:boardCoords[2][1]-bord,boardCoords[0][0]+bord:boardCoords[2][0]-bord]
		return self.img
		
	def boardView(self):
		cv2.imshow("checkmate v2", self.img)
		k = cv2.waitKey(0)
	
	def squareView(self, img):
		cv2.imshow("square", img)
		k = cv2.waitKey(0)			

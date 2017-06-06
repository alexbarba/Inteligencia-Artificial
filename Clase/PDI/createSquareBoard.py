#!/usr/bin/env python

'''
Simple programa "Generador de cuadrados para tablero de ajedrez".
Se le asigna un punto A donde inicializa el tablero, un punto B de la contraesquina y crea las coordenadas
Referencia: https://github.com/opencv/opencv/blob/master/samples/python/squares.py
'''

import numpy as np
import cv2
from boardProcess import *

def printSquares(squares, img):
	for i in squares:
		print(i, "\n")
	
def drawSquares(squares, img):
	cv2.drawContours( img, squares, -1, (0, 255, 0), 3)
	cv2.imshow('squares', img)
	cv2.waitKey(100000)

def createSquare(start, l):
	return np.array([[start[0], start[1]], \
					[start[0], start[1] + l], \
					[start[0] + l, start[1] + l], \
					[start[0] + l, start[1]]])

def createCoordsBoard(img):
	size = img.shape[:2]
	A = [0,size[1]]
	B = [size[0], size[1]-(size[1]/8)]
	x = B[0] - A[0]
	l = int(x/8)
	coords = []
	
	for j in range(8, 0, -1):
		for i in range(8):
			coords.append(createSquare([A[0] + i*l, A[1] - j*l], l))
	return coords
	
if __name__ == '__main__':
		img = cv2.imread("board.jpg")
		img = recognizeBoard(img)
		img = cv2.resize(img, (600,600))
		squares = createCoordsBoard(img)
		#print(len(squares))
		drawSquares(squares, img)
		#cv2.imwrite("board2.jpg", img)
		

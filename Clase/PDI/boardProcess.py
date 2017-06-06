#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from createSquareBoard import *
import chess
import numpy as np



def createBoardImgs(img, squares):
	size = img.shape[:2]
	A = [0,size[1]]
	B = [size[0], size[1]-(size[1]/8)]
	
	 #Crea una matriz 8x8 de imágenes del tamaño de un cuadrado cada imagen
	squareOfBoard = np.vectorize(np.zeros((int((B[0]-A[0])/8),int((A[1]-B[1])/8))))
	boardImgs = np.empty((8,8), dtype=object)
	boardImgs[:,:] = squareOfBoard
	
	x = 0
	y = 0
	for square in squares:
		boardImgs[x][y] = img[square[0][1]:square[2][1], square[0][0]:square[2][0]]
		x += 1
		if x == 8:
			y += 1
			x = 0
	return boardImgs

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
    
def detectBoard(img):
	#Devuelve los puntos A y B del cuadrado mas grande de la imagen
	#Que se considerará como el tablero
	img = cv2.GaussianBlur(img, (5, 5), 0)
	board = None
	#for gray in cv2.split(img):
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
				max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
				if max_cos < 0.1:
					board = cnt
	
	return board

def drawSquares(squares, img):
	cv2.drawContours( img, squares, -1, (0, 255, 0), 3)
	cv2.imshow('squares', img)
	cv2.waitKey(100000)
	
#def readHumanMove(before = cv2.imread("board.jpg"), after = cv2.imread("board.jpg"), board = chess.Board()):
	
def recognizeBoard(img):
	#Esta funcion encuentra el cuadrado más grande de la imagen y lo considera como el tablero, entonces devuelve la imagen del tablero
	boardCoords = detectBoard(img)
	bord = 4
	return img[boardCoords[0][1]+bord:boardCoords[2][1]-bord,boardCoords[0][0]+bord:boardCoords[2][0]-bord]
	
	
	



#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Project: Checkmate Bot
 File name: alphabeta.py
 Description:  Contiene las clases de la Inteligencia Artificial que deciden el siguiente movimiento en el ajedrez.
	
 Copyright (C) 2016 Alexis Ulises Barba Pérez, Alejandro Romero Padilla, Jose Carlos Soto Ibarra
 Universidad Marista de Guadalajara
 """
 
from ChessRules import ChessRules
from ChessBoard import ChessBoard
from copy import copy, deepcopy
import time
import sys
sys.setrecursionlimit(10000000)

class chessMove:
	def __init__(self, dad=None, fromPiece=(0,0), toPiece=(0,0), board=ChessBoard().squares, lvl=0):
		self.dad = dad
		self.fromPiece = fromPiece
		self.toPiece = toPiece
		self.board = board
		self.color = self.setColor(fromPiece)
		self.score = self.cScore()
		self.lvl = lvl
		self.children = []
		del self.board
	
	def cScore(self):
		to = self.board[self.toPiece[0]][self.toPiece[1]]
		if to != "e":
			if "P" in to: #Pawn
				return 198
			elif "R" in to: #Rook
				return 1270
			elif "T" in to: #Knight
				return 817
			elif "B" in to: #Bishop
				return 836
			elif "Q" in to: #Queen
				return 2521
			elif "K" in to:
				return 500
							
		return 0
		
	def setScore(self, newvalue):
		self.score = newvalue
		
	def setColor(self, fromTuple):
		piece = self.board[fromTuple[0]][fromTuple[1]]
		if 'w' in piece:
			return 'w'
		else:
			return 'b'
			
	def getEnemyColor(self):
		if self.color == 'w':
			return 'black'
		else:
			return 'white'

class CMtree:
	def __init__(self, lvl, board, color):
		self.lvl = lvl
		self.board = board
		self.color = color
		self.Rules = ChessRules()
		self.tree = []
		self.initTree()
		self.optime = -1
		self.nextmove = chessMove()
		
		
	def initTree(self):
		myPieces = self.getMyPiecesWithLegalMoves(self.board, self.color)
		if myPieces > 0:
			
			for f in myPieces:
				for t in self.Rules.GetListOfValidMoves(self.board,self.color,(f[0],f[1])):
					self.tree.append(chessMove(None, f, t, self.board, 0))
					toBoard = deepcopy(self.board)
					toBoard[t[0]][t[1]] = self.board[f[0]][f[1]]
					toBoard[f[0]][f[1]] = 'e'
					self.cTree(toBoard, self.tree[-1])
			
		
	def cTree(self, board, root):
		if root.lvl >= self.lvl:
			return root
		
		for f in self.getMyPiecesWithLegalMoves(board, root.getEnemyColor()):
			for t in self.Rules.GetListOfValidMoves(board,root.getEnemyColor(),(f[0],f[1])):
				root.children.append(chessMove(root, f, t, board, root.lvl+1))
				if root.children[-1].color in self.color:
					root.children[-1].setScore (root.score + root.children[-1].score)
				else:
					root.children[-1].setScore (root.score - root.children[-1].score)
					
				toBoard = deepcopy(board)
				toBoard[t[0]][t[1]] = toBoard[f[0]][f[1]]
				toBoard[f[0]][f[1]] = 'e'
				self.cTree(toBoard, root.children[-1])
					
	def getMyPiecesWithLegalMoves(self,board,color):
		#get list of my pieces
		myPieces = []
		for row in range(8):
			for col in range(8):
				piece = board[row][col]
				if color[0] in piece:
					if len(self.Rules.GetListOfValidMoves(board,color,(row,col))) > 0:
						myPieces.append((row,col))	
		
		return myPieces
	
	def alphabeta(self, n, alpha, beta):
		if (n.children):
			if (n.color == self.color):
				for i in n.children:
					alpha = max(self.alphabeta(i,alpha,beta),alpha)
					if(alpha>=beta):
						return beta
				return alpha
			else:
				for i in n.children:
					beta = min(self.alphabeta(i,alpha,beta),beta)
					if(alpha>=beta):
						return alpha
				return beta
		else:
			return n.score
	
	
	
	def route(self):
		def recursive(n):
			if n.dad:
				if (n.dad.dad):
					return recursive(n.dad)
				else:
					return n.dad
				
		for i in self.leafs:
			if(i.score==self.optime):
				self.nextmove = recursive(i)
				
	def run_alphabeta(self):
		for i in self.tree:
			temp = self.alphabeta(i, -9000, 9951)
			#temp = self.alphabeta(i)
			if temp > self.optime:
				self.optime = temp
				self.nextmove = i
		#print(self.optime)
		#self.route()




	

def printTree(n):
	if n.children:
		for i in n.children:
			printTree(i)
	print(n.fromPiece, n.toPiece)
	cont += 1

			
def AI(board, color):
	lvl = 2
	#board = ChessBoard().squares
	#color = 'white'
	#start_time = time.time()
	cmtree = CMtree(lvl, board, color)
	cmtree.run_alphabeta()
	'''
	for i in cmtree.tree:
		print('padre: ',i.fromPiece, i.toPiece, i.score)
		for j in i.children:
			print('hijo: ',j.fromPiece, j.toPiece, j.score)
			
	print('best move: ', cmtree.nextmove.fromPiece, cmtree.nextmove.toPiece, i.score)
	print('best score: ', cmtree.optime)
	'''
	return cmtree
	#print("--- %s seconds ---" % (time.time() - start_time))
'''
#debug		
board = [['e','e','e','e','e','e','e','e'],\
		['e','e','e','e','e','e','e','e'],\
		['e','e','e','e','e','e','e','e'],\
		['bP','bP','bP','bR','bQ','bP','bP','bP'],\
		['wP','wP','wP','wP','wP','wP','wP','wP'],\
		['e','e','e','e','e','e','e','e'],\
		['e','e','e','e','e','e','e','e'],\
		['e','e','e','e','e','e','e','e']]

AI(board, 'white')

		
'''

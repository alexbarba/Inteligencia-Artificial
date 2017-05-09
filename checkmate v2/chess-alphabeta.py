import chess
import chess.pgn
import chess.uci
import chess.svg
import spur
import chess.polyglot
import os
clear = lambda: os.system('clear')

class chessAI:
	def __init__(self, lvl = 3, color = True):
		self.lvl = lvl
		self.color = color
		self.book = chess.polyglot.open_reader("/home/alex/Documents/ai/python-chess/data/polyglot/performance.bin")
		self.apertura = 10 #Turnos que aprovechara de libros de apertura
	def alphaBeta(self, board, alpha, beta, rlvl):
		if board.fullmove_number - rlvl >= self.lvl:
			return self.boardEvaluation(board)
		
		for i in board.legal_moves:
			board.push(i)
			current_eval = self.alphaBeta(board, alpha, beta, rlvl)
			board.pop()
			
			if current_eval >= beta:
				return beta
			
			if current_eval > alpha:
				alpha = current_eval
			
		return alpha
	
	def rootAI(self, board):
		
		#Si no han pasado 10 turnos utiliza una apertura de libro
		if board.fullmove_number > self.apertura:
			return self.rootAlphaBeta(board)
			
		#Si no, usa alphabeta
		elif board.fullmove_number <= self.apertura:
			try:
				return(self.book.find(board).move())
			except IndexError:
				self.book.close()
				self.book = chess.polyglot.open_reader("/home/alex/Documents/ai/python-chess/data/polyglot/gm2001.bin")
				print("Aperturas gm2001")
				try:
					return(self.book.find(board).move())
				except IndexError:
					self.book.close()
					self.book = chess.polyglot.open_reader("/home/alex/Documents/ai/python-chess/data/polyglot/rodent.bin")
					print("Aperturas rodent")
					try:
						return(self.book.find(board).move())
					except IndexError:
						self.book.close()
						self.book = chess.polyglot.open_reader("/home/alex/Documents/ai/python-chess/data/polyglot/komodo.bin")
						print("Aperturas komodo")
						try:
							return(self.book.find(board).move())
						except IndexError:
							return self.rootAlphaBeta(board)	
			
			
	def rootAlphaBeta(self, board):
			best_move = None
			max_eval = float('-infinity')
			
			count = 0
			for move in board.legal_moves:
				board.push(move)
				current_eval = self.alphaBeta(board, float('-infinity'), float('infinity'), board.fullmove_number - 1)
				board.pop()
				count += 1
				clear()
				print(board)
				print(str(count/len(board.legal_moves)*100) + "% completado")

				if current_eval > max_eval:
					max_eval = current_eval
					best_move = move

			return best_move
			
	def boardEvaluation(self, board):
		#Tipos de pieza PAWN = 1, KNIGHT = 2, BISHOP = 3, ROOK = 4, QUEEN = 5, KING = 6
		#Color de jugador WHITE = True, BLACK = False
		wMaterialScore = len(board.pieces(1,True)) + \
							len(board.pieces(2,True)) * 3 + \
							len(board.pieces(3,True)) * 3 + \
							len(board.pieces(4,True)) * 5 + \
							len(board.pieces(5,True)) * 9 + \
							len(board.pieces(3,True)) * 200
							
		bMaterialScore = len(board.pieces(1,False)) + \
							len(board.pieces(2,False)) * 3 + \
							len(board.pieces(3,False)) * 3 + \
							len(board.pieces(4,False)) * 5 + \
							len(board.pieces(5,False)) * 9 + \
							len(board.pieces(3,False)) * 200
		if self.color:
			return wMaterialScore - bMaterialScore
		return bMaterialScore - wMaterialScore


class player:
	def __init__(self, color):
		self.color = color
		if self.color:
			self.playerType = int(input("White is a: \n1) Human \nother) AI\n"))
		else:
			self.playerType = int(input("Black is a: \n1) Human \nother) AI\n"))
		
		if self.playerType != 1:
			self.AI = chessAI(int(input("Lvl de AI (Entero): ")),self.color)
			
	def move(self, board):
		if self.playerType == 1: #Si es humano
			self.moveHuman(board)
		else:
			self.moveAI(board)
			
	def moveHuman(self, board):
		legal_moves = []
		moveNumber = 0
		
		for i in board.legal_moves:
			legal_moves.append(i)
			print(str(moveNumber) + ") " + str(i))
			moveNumber += 1
		
		while(True):
			try:
				moveNumber = int(input("Elige un movimiento: "))
				board.push(legal_moves[moveNumber])
				break
			except (TypeError, IndexError, ValueError):
				print("Introduzca un valor válido.")
		
		
	def moveAI(self, board):
		board.push(self.AI.rootAI(board))

class game:
	def __init__(self, board = chess.Board()):
		self.board = board
			
	def startgame(self):
		whitePlayer = player(True)
		blackPlayer = player(False)
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
		
		print("El resultado es: " + self.board.result())

game().startgame()


	
	


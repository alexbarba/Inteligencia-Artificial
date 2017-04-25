from ChessRules import ChessRuless
import random

class node:
	def __init__(self, dad, fromPiece, toPiece, board, lvl):
		self.dad = dad
		self.fromPiece = fromPiece
		self.toPiece = toPiece
		self.board = board
		selc.color = setColor(fromPiece)
		self.score = cScore(fromPiece, toPiece, board)
		self.lvl = lvl
	
	children = []
	
	def cScore(toTuple, board):
		toPiece = board[toTuple[0]][toTuple[1]]
		if toPiece != "e":
			if "P" in toPiece: #Pawn
				return 198
			elif "R" in toPiece: #Rook
				return 1270
			elif "T" in toPiece: #Knight
				return 817
			elif "B" in toPiece: #Bishop
				return 836
			elif "Q" in toPiece: #Queen
				return 2521
			elif "K" in toPiece:
				return 500
							
		return 0
		
	def setColor(fromTuple):
		piece = board[fromTuple[0]][fromTuple[1]]
		if 'w' in piece:
			return 'w'
		else:
			return 'b'

class CMtree:
	def __init__(self, lvl, board, color):
		self.lvl = lvl
		self.board = board
		self.color = color
		self.tree = initTree(lvl, board, color)
		
	def initTree(diff, board, color):
		myPieces = getMyPiecesWithLegalMoves(board, color)
		if myPieces > 0:
			roots = []
			for f in myPieces:
				for t in Rules.GetListOfValidMoves(board,color,(f[0],f[1])):
					roots.append(node(None, f, t, board, 0))
					toBoard[t[0]][t[1]] = fromPiece
					toBoard[f[0]][f[1]] = 'e'
					cTree(diff, toBoard, roots[-1])
			return roots
		return None
		
	def cTree(diff, board, root):
		if root.lvl >= diff:
			return root
		
		for f in getMyPiecesWithLegalMoves(board, color):
			for t in Rules.GetListOfValidMoves(board,color,(f[0],f[1])):
				root.childrens.append(node(root, f, t, board, root.lvl))
				toBoard[t[0]][t[1]] = fromPiece
				toBoard[f[0]][f[1]] = 'e'
				cTree(diff, toBoard, root.childrens[-1])
				
		
			
	def getMyPiecesWithLegalMoves(self,board,color):
		if color == "black":
			myColor = 'b'
		else:
			myColor = 'w'
			
		#get list of my pieces
		myPieces = []
		for row in range(8):
			for col in range(8):
				piece = board[row][col]
				if myColor in piece:
					if len(self.Rules.GetListOfValidMoves(board,color,(row,col))) > 0:
						myPieces.append((row,col))	
		
		return myPieces
		
		
def alphabeta():
	lvl = 2
	board = ChessBoard()
	color = 'white'
	tree = CMtree(lvl, board, color)
	for i in tree:
		for j in tree.children:
			print (j.fromPiece)
			
		
alphabeta()

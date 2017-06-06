
	
class move():
	def __init__(self, player = 'x', board = [['', '', ''],['', '', ''],['', '', '']], x, y):
		self.player = player
		self.board = board
		self.writeBoard(self.player, x, y)
		
	def posibleMoves(self):
		moves = []
		tam = 3
		for i in range(tam):
			for j in range(tam):
				if self.board[i][j] == '':
					moves.append((i,j))
		return moves
		
	def writeBoard(self, player, x, y):
		if self.board[x][y] == '':
			self.board[x][y] = player
		
class tictacIA(player):
	def __init__(self, player = 'x', board = [['', '', ''],['', '', ''],['', '', '']], lvl = 2):
		self.player = player()
		self.board = board
		self.score = 8
		self.lvl = lvl
		self.nextmove
		self.optime
		
	def writeBoard(self, player, x, y):
		if self.board[x][y] == '':
			self.board[x][y] = player

	def printBoard(self):
		for i in self.board:
			print(i)
			
	def endGame(self):
		if '' in board:
			return False
		return True
	
	def whoWin(self):
		if self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x' or \
		self.board[2][0] == 'x' and self.board[1][1] == 'x' and self.board[0][2] == 'x':
			return 'x'
		
		if self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o' or \
		self.board[2][0] == 'o' and self.board[1][1] == 'o' and self.board[0][2] == 'o':
			return 'x'
		
		tam = 3
		for x in range(tam):
			if self.board[x][0] == 'x' and self.board[x][1] == 'x' and self.board[x][2] == 'x' or \
			self.board[0][x] == 'x' and self.board[1][x] == 'x' and self.board[2][x] == 'x':
				return 'x'
			elif self.board[x][0] == 'o' and self.board[x][1] == 'o' and self.board[x][2] == 'o' or \
			self.board[0][x] == 'o' and self.board[1][x] == 'o' and self.board[2][x] == 'o':
				return 'o'
		
		if self.endGame():
			return 'xo'
		
		return 0
			
	def getEnemy(self):
		if self.player == 'x':
			return 'o'
		else:
			return 'x'
		
	def setScore(self):
		self.score = cScore(self.board)
		
	def cScore(self, board):
		possiblesLines = 8
		
		if self.board[0][0] == self.getEnemy() or board[1][1] == self.getEnemy() or board[2][2] == self.getEnemy():
			possiblesLines-=1
		if self.board[2][0] == self.getEnemy() or board[1][1] == self.getEnemy() or board[0][2] == self.getEnemy():
			possiblesLines-=1
		
		tam = 3
		for x in range(tam):
			if board[x][0] == self.getEnemy() or board[x][1] == self.getEnemy() or board[x][2] == self.getEnemy():
				possiblesLines-=1
			if board[0][x] == self.getEnemy() or board[1][x] == self.getEnemy() or board[2][x] == self.getEnemy():
				possiblesLines-=1
		
		return possiblesLines
	
	def posibleMoves(self):
		moves = []
		tam = 3
		for i in range(tam):
			for j in range(tam):
				if self.board[i][j] == '':
					moves.append((i,j))
		return moves
		
	def alphabeta(self, n, alpha, beta):
		if (n.possibleMoves()):
			if (n.player == self.player):
				for i in n.possibleMoves():
					m = move(n.getEnemy, n.board, i[0], i[1])
					alpha = max(self.alphabeta(m,alpha,beta),alpha)
					if(alpha>=beta):
						return beta
				return alpha
			else:
				for i in n.possibleMoves():
					m = move(n.getEnemy, n.board, i[0], i[1])
					beta = min(self.alphabeta(m,alpha,beta),beta)
					if(alpha>=beta):
						return alpha
				return beta
		else:
			return cScore(n.board)
			
	def run_alphabeta(self):
		for i in self.posibleMoves():
			m = move(n.getEnemy, n.board, i[0], i[1])
			temp = self.alphabeta(m, -8, 8)
			#temp = self.alphabeta(i)
			if temp > self.optime:
				self.optime = temp
				self.nextmove = i
		#print(self.optime)
	

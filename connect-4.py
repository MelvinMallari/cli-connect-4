class Board:
  def __init__(self, rows=6, cols=7):
    self.rows = rows
    self.cols = cols
    self.board = [['-'] * self.rows for _ in range(self.cols)]
    self.piecesRemaining = self.rows*self.cols
  
  def __str__(self):
    res = "\n"
    # Transpose the board, then print:
    transpose = self.transpose(self.board)
    for i in range(len(transpose)-1,-1,-1):
      row = " ".join(transpose[i])
      res += row + '\n'
    lastRow = [str(i+1) for i in range(self.cols)]
    res += " ".join(lastRow)
    res += "\n"
    return res

  def transpose(self, arr):
    rows, cols  = len(arr), len(arr[0])
    transpose = []
    for c in range(cols):
      newRow = []
      for r in range(rows):
        newRow.append(arr[r][c])
      transpose.append(newRow)
    return transpose

  def mirror(self, arr):
    mirror = []
    for i in range(len(arr)):
      row = []
      for j in range(len(arr[0])-1, -1, -1):
        row.append(arr[i][j])
      mirror.append(row)
    return mirror
      

  def isFull(self):
    return self.piecesRemaining == 0
  
  def validCol(self, col):
    if 1 <= col <= self.cols: return True
    print("Invalid Col")
    return False
  
  def validSymbol(self, symbol):
    return symbol.upper() in ['X', 'O']

  def put(self, col, symbol):
    if self.validCol(col) and self.validSymbol(symbol):
      for row in range(self.rows):
        if self.board[col-1][row] == '-':
          self.board[col-1][row] = symbol
          self.piecesRemaining -= 1
          return True
    return False

  def isWon(self):
    return self.verticalCheck(self.board) or self.horizontalCheck(self.board) or self.diagonalCheck()
  
  def verticalCheck(self, board):
    for i in range(len(board)):
      counter = 0
      currSymbol = None
      for j in range(len(board[0])):
        if board[i][j] == '-': 
          continue
        else:
          if currSymbol == None:
            currSymbol = board[i][j]
            counter = 1
          elif currSymbol == board[i][j]:
            counter += 1
          else: 
            currSymbol = board[i][j]
            counter = 1
          if counter == 4: return True
    return False

  def horizontalCheck(self, board):
    transpose = self.transpose(board)
    return self.verticalCheck(transpose)

  def fDiagCheck(self, board):
    col, row = len(board[0]), len(board)
    fdiag = [[] for _ in range(col + row - 1)]
    for i in range(col):
      for j in range(row):
        fdiag[i+j].append(board[j][i])
    
    for diag in fdiag:
      if len(diag) < 4: continue
      for i in range(len(diag) - 3):
        if self.validSymbol(diag[i]) and diag[i] == diag[i+1] == diag[i+2] == diag[i+3]:
          return True
    return False

  def dDiagCheck(self, board):
    mirror = self.mirror(board)
    return self.fDiagCheck(mirror)

  def diagonalCheck(self):
    return self.fDiagCheck(self.board) or self.dDiagCheck(self.board)

class ConnectFour:
  def __init__(self):
    self.board = Board()
    self.currentPlayer = "X"

  def togglePlayer(self):
    if self.currentPlayer == "X":
      self.currentPlayer = "O"
    else: 
      self.currentPlayer = "X"

  def getInput(self):
    print(self.board)
    col = input("Input col (1-7): ")
    if self.board.put(int(col), self.currentPlayer):
      self.togglePlayer()
    else:
      print("Invalid Column")
      self.getInput()
  
  def gameWon(self):
    if self.board.isWon():
      self.togglePlayer()
      print('\n')
      print("Congrats Player {}!".format(self.currentPlayer))
      print(self.board)
      return True
    return False

  def gameTie(self):
    if self.board.isFull():
      print('\n')
      print("Tie Game")
      print(self.board)
      return True
    return False
  
  def play(self):
    print("Welcome to CLI Connect 4!")
    while True:
      if self.gameWon(): break
      if self.gameTie(): break
      self.getInput()
    print("Thanks for playing!")

ConnectFour().play()

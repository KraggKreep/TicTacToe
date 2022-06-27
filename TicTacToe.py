mainBoard = [["-","-","-"],["-","-","-"],["-","-","-"]]

def displayBoard():
  for lane in mainBoard:
    print(lane)
  print("")

def isBoardFull():
  boardIsFull = True

  for row in mainBoard:
    for item in row:
      if item == "-":
        boardIsFull = False
        return boardIsFull

  return boardIsFull

def threeInARowCheck(scoreList):
  isAWin = False
  if scoreList[0] == "x" and scoreList[1] == "x" and scoreList[2] == "x":
    isAWin = True
  elif scoreList[0] == "o" and scoreList[1] == "o" and scoreList[2] == "o":
    isAWin = True

  return isAWin
      

def isGameOver():
  if isBoardFull():
    return True
  topRow = [mainBoard[0][0], mainBoard[0][1], mainBoard[0][2]]
  middleRow = [mainBoard[1][0], mainBoard[1][1], mainBoard[1][2]]
  bottomRow = [mainBoard[2][0], mainBoard[2][1], mainBoard[2][2]]

  leftColumn = [mainBoard[0][0], mainBoard[1][0], mainBoard[2][0]]
  middleColumn = [mainBoard[0][1], mainBoard[1][1], mainBoard[2][1]]
  rightColumn = [mainBoard[0][2], mainBoard[1][2], mainBoard[2][2]]

  diagOne = [mainBoard[0][0], mainBoard[1][1], mainBoard[2][2]]
  diagTwo = [mainBoard[0][2], mainBoard[1][1], mainBoard[2][0]]

  if threeInARowCheck(topRow) or threeInARowCheck(middleRow) or threeInARowCheck(bottomRow):
    return True
  elif threeInARowCheck(leftColumn) or threeInARowCheck(middleColumn) or threeInARowCheck(rightColumn):
    return True
  elif threeInARowCheck(diagOne) or threeInARowCheck(diagTwo):
    return True

  return False

def makePlayerMove(theMove):
  row = 0
  column = 0
  
  x = theMove.split()
  
  if x[0] == "middle":
    row = 1
  elif x[0] == "bottom":
    row = 2

  if x[1] == "middle":
    column = 1
  elif x[1] == "right":
    column = 2
    
  mainBoard[row][column] = "x"

def makeComputerMove():
  #make random move that isn't occupied by player move
  for row in mainBoard:
    for item in row:
      if item == "-":
        item = "o"
        return
    

def GameLoop():
  playerMove = input("You are x's. What is your move?")
  print("")
  makePlayerMove(playerMove)
  if isGameOver():
    #end Game
    displayBoard()
    print("Game Over, you Win")
    return
  
  makeComputerMove()
  
  if isGameOver():
    #end Game
    displayBoard()
    print("Game Over, you lose")
    return
  else:
    displayBoard()
    GameLoop()
    



displayBoard()
GameLoop()






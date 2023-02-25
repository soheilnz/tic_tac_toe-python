import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
curPlayer = "X"
winner = None
gameRun = True


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board [6] + " | " + board[7] + " | " + board[8])
    print("---------")


def playerInput(board):
    inp = int(input("Enter a number between 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1]=="-":
        board[inp-1] = curPlayer
        return True
    else:
        print("Oops try another place!")
        return False

def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True
    gameRun = False


def checkcol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board [8] and board[2] != "-":
        winner = board[2]
        return True
    gameRun = False


def checkDiagnol(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    gameRun = False
    

def checkTie(board):
    global gameRun
    if "-" not in board:
        printBoard(board)
        print("it's a tie")
        gameRun = False


def switch():
    global curPlayer
    if curPlayer == "X":
        curPlayer = "O"
    else:
        curPlayer = "X"


def computer(board):
    while curPlayer == "O":
        poss = random.randint(0, 8)
        if board[poss] == "-":
            board[poss] = "O"
            switch()


def checkWin():
    global gameRun
    if checkRow(board) or checkcol(board) or checkDiagnol(board):
        gameRun = False
        printBoard(board)
        print(f"the winner is {winner}")



while gameRun:
    printBoard(board)
    if playerInput(board):
        checkWin()
        checkTie(board)
        switch()
        computer(board)
        checkWin()
        checkTie(board)
    
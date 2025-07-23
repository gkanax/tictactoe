import tkinter
import random
import pdb
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# making of the GUI
window = tkinter.Tk()
window.configure(bg="#D9EAFD")
window.title("TicTacToe")
window.minsize(width=350, height=230)
window.iconbitmap("TicTacToe.ico")
window.grid()

matrix = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9]   # Row 3
]
Game = True

def chooseRandomNumber():
    randomRaw = random.randint(0,2)
    randomColumn = random.randint(0,2)
    matrixPosition = (randomRaw, randomColumn)
    
    while (matrix[randomRaw][randomColumn] == "X" or matrix[randomRaw][randomColumn] == "O"):
        randomRaw = random.randint(0,2)
        randomColumn = random.randint(0,2)
        matrixPosition = (randomRaw, randomColumn)
    print(matrixPosition)
    return matrixPosition

def isChoiseAlreadyThere(choice):
    print("isChoiseAlreadyThere")
    
def placeInBoard(choice, sign):
    raw, column = choice
    current = buttons[raw][column].cget("text")
    if current == "":
        buttons[raw][column].config(text=sign)
    else:
        pass

def checkResult(choice, sign):
    positionR, positionC = choice
    matrix[positionR][positionC] = sign
    print(f'CheckResult:{sign}')

    if (matrix[0][0] == matrix[0][1] == matrix[0][2] == "X"):
        Game = False
    elif (matrix[0][0] == matrix[0][1] == matrix[0][2] == "O"):
        Game = False
    elif (matrix[1][0] == matrix[1][1] == matrix[1][2] == "X"):
        Game = False
    elif (matrix[1][0] == matrix[1][1] == matrix[1][2] == "O"):
        Game = False
    elif (matrix[2][0] == matrix[2][1] == matrix[2][2] == "X"):
        Game = False
    elif (matrix[2][0] == matrix[2][1] == matrix[2][2] == "O"):
        Game = False
    elif (matrix[0][0] == matrix[1][0] == matrix[2][0] == "X"):
        Game = False
    elif (matrix[0][0] == matrix[1][0] == matrix[2][0] == "O"):
        Game = False
    elif (matrix[0][1] == matrix[1][1] == matrix[1][2] == "X"):
        Game = False
    elif (matrix[0][1] == matrix[1][1] == matrix[1][2] == "O"):
        Game = False
    elif (matrix[0][2] == matrix[1][2] == matrix[2][2] == "X"):
        Game = False
    elif (matrix[0][2] == matrix[1][2] == matrix[2][2] == "O"):
        Game = False
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == "X"):
        Game = False
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == "O"):
        Game = False
    elif (matrix[2][0] == matrix[1][1] == matrix[0][2] == "X"):
        Game = False
    elif (matrix[2][0] == matrix[1][1] == matrix[0][2] == "O"):
        Game = False
    else:
        Game = True
    return Game

def playTheGame():
    #pdb.set_trace()
    global Game 
    global playerFirst

    if signChoice == 1: # X
        print("Player choice is X")
        global sign 
        sign = "X"
        global oppontentSign
        oppontentSign = "O" 
        global turn
        turn = 0
        while (Game == True):
            turn = turn + 1
            print(playerFirst)
            if playerFirst == 1: #wait for the opponent to click
                print("Wait for you to play")
                Game = False
                playerFirst = 0
            else:
                playerFirst = 1
                choice = chooseRandomNumber()
                print(choice)
                placeInBoard(choice, sign)
                Game = checkResult(choice, sign)
                print("Player will wait for opponent")
    elif signChoice == 2: # O
        print("Player's choise is O")
        sign = "O"
        oppontentSign = "X"  
        while (Game == True):
            print(playerFirst)
            if playerFirst == 1: #wait for the opponent to click
                print("Wait for you to play")
                Game = False
                playerFirst = 0
            else:
                playerFirst = 1
                choice = chooseRandomNumber()
                print(choice)
                placeInBoard(choice, oppontentSign)
                Game = checkResult(choice, oppontentSign)
                print("Player will wait for opponent")             

# Configure grid columns to expand
for i in range(8):
    window.grid_columnconfigure(i, weight=1)

# Game options, Choose either O or X and if you start first
Sign = tkinter.IntVar()
Sign.set(1) #Default sign
signLabelX = tkinter.Radiobutton(window, text="Choose X", variable=Sign, value = 1, font=("Calibri", 10), bg="#D9EAFD") 
signLabelX.grid(row=0, column=0, sticky='w')

signLabelO = tkinter.Radiobutton(window, text="Choose O", variable=Sign, value = 2, font=("Calibri", 10), bg="#D9EAFD") 
signLabelO.grid(row=0, column=1, sticky='w')

firstToPlay = tkinter.IntVar()
#firstToPlay.set(1) # Default to "Play First"
firstToPlayLabel = tkinter.Radiobutton(window, text="Play First", variable=firstToPlay, value =1, font=("Calibri", 10), bg="#D9EAFD")
firstToPlayLabel.grid(row=0, column=2, sticky='w')

# label for Score
scoreLabel = tkinter.Label(text="Score:", font=("Calibri", 12), bg="#D9EAFD")
scoreLabel.grid(row=1, column=0, sticky='w', padx=5, pady=5)

# Start/Restart button
startRestartButton = tkinter.Button(text = "Start/Restart", font=("Calibri", 10, "bold"),
                                     command = playTheGame, bg="#D9EAFD")
startRestartButton.grid(row=1, column=5, pady=5,padx=5,sticky='e')

# 3x3 grid of buttons
buttons = []
signChoice = Sign.get()
playerFirst = firstToPlay.get()

def on_click(r, c, sign):
    #sign = sign
    #choice = r,c
    current = buttons[r][c].cget("text")
    if current == "":
        buttons[r][c].config(text=oppontentSign)
        choice = r,c
        global turn
        global Game
        global playerFirst 
        if (turn % 2 != 0) and playerFirst:
            Game = checkResult(choice, sign)
            print(f'Game is: {Game}')
            playerFirst = 0
            playTheGame()
        elif (turn % 2 == 0) and playerFirst:
            Game = checkResult(choice, oppontentSign)
            print(f'Game is: {Game}')
            playerFirst = 0
            playTheGame()
        elif (turn % 2 != 0) and (playerFirst == 0):
            Game = checkResult(choice, sign)
            print(f'Game is: {Game}')
            playerFirst = 0
            playTheGame()
        elif (turn % 2 == 0) and (playerFirst == 0):
            Game = checkResult(choice, oppontentSign)
            print(f'Game is: {Game}')
            playerFirst = 0
            playTheGame()
    
board_size = 3

for row in range(2, board_size + 2):
    row_buttons = []
    for col in range(1, board_size + 1):
        btn = tkinter.Button(window, text="", width=4, height=1,
                             font=("Calibri", 14),
                             command=lambda r=row, c=col: on_click(r-2 , c-1, sign))
        btn.grid(row=row, column=col, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

window.mainloop()
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
numberOfMoves = 0

def chooseRandomNumber():
    randomRaw = random.randint(0,2)
    randomColumn = random.randint(0,2)
    matrixPosition = (randomRaw, randomColumn)
    
    while (matrix[randomRaw][randomColumn] == "X" or matrix[randomRaw][randomColumn] == "O"):
        randomRaw = random.randint(0,2)
        randomColumn = random.randint(0,2)
        matrixPosition = (randomRaw, randomColumn)
    return matrixPosition
    
def placeInBoard(choice, sign):
    raw, column = choice
    current = buttons[raw][column].cget("text")
    if current == "":
        buttons[raw][column].config(text=sign)
    else:
        scoreLabel.config(text="You lost dear!")

def startOrRestartTheGame():
    if Game == False:
        restartGame()
    else:
        playTheGame()

def restartGame():
    global matrix, Game, turn, sign, oppontentSign, playerFirst, numberOfMoves
    # Reset the matrix to empty cells
    matrix = [["", "", ""], ["", "", ""], ["", "", ""]]
    # Reset all buttons to empty and re-enable them
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="normal")
    # Reset game variables
    Game = True
    turn = 0  # Reset turn counter
    playerFirst = firstToPlay.get()  # Assume Player 1 starts
    if signChoice == 1: # X
        sign = "X"
        oppontentSign = "O" 
    else:
        sign = "O"
        oppontentSign = "X" 
    numberOfMoves = 0
    print("Game restarted.")

def disableButtons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state="disabled")  # Disable each button

def endGame():
    disableButtons()
    
def checkResult(choice, sign):
    positionR, positionC = choice
    matrix[positionR][positionC] = sign
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
    elif (matrix[0][1] == matrix[1][1] == matrix[2][1] == "X"):
        Game = False
    elif (matrix[0][1] == matrix[1][1] == matrix[2][1] == "O"):
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
    global Game, playerFirst, sign, oppontentSign, turn, numberOfMoves
    if numberOfMoves == 0:
        playerFirst = firstToPlay.get()  # Get who plays first (1 for Player 1, 0 for Player 2)
        sign = Sign.get()
    if signChoice == 1: # X
        sign = "X"
        oppontentSign = "O" 
        turn = 0
        while (Game == True):
            turn = turn + 1
            if playerFirst == 1: #wait for the opponent to click
                Game = False
                playerFirst = 0
            else:
                playerFirst = 1
                choice = chooseRandomNumber()
                placeInBoard(choice, sign)
                Game = checkResult(choice, sign)
                if Game == False:
                    scoreLabel.config(text="You lost dear!")
                    endGame()
                elif Game and numberOfMoves == 4:
                    scoreLabel.config(text="DRAW-No6")
                    endGame()
    elif signChoice == 2: # O
        sign = "O"
        oppontentSign = "X"  
        turn = 0
        while (Game == True):
            turn = turn + 1
            if playerFirst == 1: #wait for the opponent to click
                Game = False
                playerFirst = 0
            else:
                playerFirst = 1
                choice = chooseRandomNumber()
                placeInBoard(choice, oppontentSign)
                Game = checkResult(choice, oppontentSign)
                if Game == False:
                    endGame()
                    scoreLabel.config(text="You lost dear!")
                elif Game and numberOfMoves == 4:
                    scoreLabel.config(text="DRAW-No7")
                    endGame()       

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
                                     command = startOrRestartTheGame, bg="#D9EAFD")
startRestartButton.grid(row=1, column=5, pady=5,padx=5,sticky='e')

# 3x3 grid of buttons
buttons = []
signChoice = Sign.get()
playerFirst = firstToPlay.get()

def on_click(r, c, sign):
   
    current = buttons[r][c].cget("text")
    if current == "":
        buttons[r][c].config(text=oppontentSign)
        choice = r,c
        global turn, Game, playerFirst, numberOfMoves
        numberOfMoves = numberOfMoves + 1
        if (turn % 2 == 0) and playerFirst:
            Game = checkResult(choice, oppontentSign)
            if Game and numberOfMoves == 4:
                scoreLabel.config(text="DRAW!")
                endGame()  
            elif Game == False:
                scoreLabel.config(text="You win!")
                endGame()
            playerFirst = 0
            playTheGame()
        elif (turn % 2 == 0) and (playerFirst == 0):
            Game = checkResult(choice, oppontentSign)
            if Game and numberOfMoves == 5:
                scoreLabel.config(text="DRAW!")
                endGame()
                restartGame()  
            elif Game == False:
                print("You win!")
                scoreLabel.config(text="You win!")
                endGame()
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
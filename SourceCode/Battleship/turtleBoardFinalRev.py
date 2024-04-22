import turtle as t
from turtle import *
from Directions_Text import Directions_Text 

player1Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
player2Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

#puts the ships on the board for player 1
for i in range(3):
    player1Board[0][0+i] = '='
for i in range(3):
    player1Board[1][7+i] = '='
for i in range(4):
    player1Board[2+i][2] = '='
for i in range(5):
    player1Board[8][3+i] = '='
for i in range(2):
    player1Board[3+i][5] = '='

#puts the ships on the board for player 2
for i in range(3):
    player2Board[6][4+i] = '='
for i in range(3):
    player2Board[4+i][0] = '='
for i in range(4):
    player2Board[1+i][9] = '='
for i in range(5):
    player2Board[2][0+i] = '='
for i in range(2):
    player2Board[0][3+i] = '='

wn = t.Screen()
wn.setup(width = 1000, height = 1000)

w = 40

#Drawing Turtle Config -
draw = t.Turtle()
draw.speed("fastest")
draw.penup()

playerTurn = True
listOfTurts = []
turtRows = []
turtColumn = []
#gets a list of the turtles in the board
for turt in listOfTurts:
    turtRows.append((listOfTurts.index(turt)//10))
    turtColumn.append((listOfTurts.index(turt)%10))


turt = t.Turtle(shape='square')

def drawplayerBoard(turn,y):
    global player1Board, player1Board
    #making player 1's board
    if turn == 1:
        board = player1Board
    #making player 2's board
    else:
        board = player2Board
    x,y = -400,y
    for row in board:
        for col in row:
            turt = t.Turtle(shape='square')
            turt.penup()
            turt.onclick(gaming_w_Clicks)
            turt.shapesize(1.3,1.3,4)
            turt.speed('fastest')
            turt.goto(x,y)
            listOfTurts.append(turt)
            # if col == "=":
            #     turt.fillcolor('#3b3a3a')
            # else:
            turt.fillcolor("#ffffff")

            x += w
        y -= w
        x = -400
    turt.penup()

#Set Keys/Buttons -
currPlaya = 1
def gaming_w_Clicks(x,y):
    global currPlaya, playerTurn
    #if Player 1 is going
    if playerTurn == True:
        if noShips(player2Board): #if no ships are detected on Player 2s board
            draw.setpos(25,-100)
            draw.write("Player 1 wins"
                       "Credits:"
                       "Gracey Kippling"
                       "Kai Howard"
                       "The Bandalorian"
                       "https://www.youtube.com/watch?v=nsLTQj-l_18&feature=youtu.be"
                       "Featuring Static Method at the end",font=("Verdana", 15))
            draw.penup()
            draw.setpos(1000,1000)
            # break
        playerTurn = False
    #if Player 2 is going
    elif playerTurn == False:
        if noShips(player1Board): #if no ships are detected on Player 1s board
            draw.setpos(25,-100)
            draw.write("Player 2 wins"
                       "Credits:"
                       "Gracey Kippling"
                       "Kai Howard"
                       "The Bandalorian"
                       "https://www.youtube.com/watch?v=nsLTQj-l_18&feature=youtu.be"
                       "Featuring Static Method at the end",font=("Verdana", 15))
            draw.penup()
            draw.setpos(1000,1000)
            # break
        playerTurn = True

    for turt in listOfTurts:
        hit = 'red'
        miss = 'blue'
        #makes sure you are clicking in the square, if you click between them it gets a bit screwed up
        if (turt.xcor()-25 < x < turt.xcor() +25) and (turt.ycor()-25 < y < turt.ycor() +25):
            
            #grabs the index for where you click in the list of boards
            row = (listOfTurts.index(turt)//10)
            column = (listOfTurts.index(turt)%10)
            
            #makes the game to where board 1 can be clicked once then its board 2 that can be clicked once, then it goes back till
            #   the end of the game. but you can click on a hit or miss space and it still works (bug)
            #if the row clicked is above or equal to 10 and the current player is 2
            if row >= 10 and currPlaya == 2:
                #change current player  1
                currPlaya = 1
                #makes the rows work as if the board was its own entity
                #   Ex: row 11 (in list) - 10 becomes row 1 (as a board)
                row -= 10
                #if player clicks a ship
                if player2Board[row][column] == "=":
                    #the square becomes red
                    turt.fillcolor(hit)
                    #board list index becomes an X for noShips function later on
                    player2Board[row][column] = "X"
                #if player clicks and misses a ship
                elif player2Board[row][column] == " ":
                    #the square becomes blue
                    turt.fillcolor(miss)
                    #board list index becomes an O for noShips function later on
                    player2Board[row][column] = "O"

            elif row < 10 and currPlaya == 1:
                currPlaya = 2
                if player1Board[row][column] == "=":
                    turt.fillcolor(hit)
                    player1Board[row][column] = "X"
                    print(player1Board[row][column])

                elif player1Board[row][column] == " ":
                    turt.fillcolor(miss)
                    player1Board[row][column] = "O"
                    print(player1Board[row][column])


def noShips(board):
    #if the board is full then it will be a tie
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "=":
                #there are still ships on the board
                return False
    #there are no more ships on the board and a player has won
    return True
#Call Functions -
drawplayerBoard(1,400)
drawplayerBoard(2,-50)
Directions_Text.labLeft(draw)
Directions_Text.labRight(draw)
draw.penup()
draw.goto(1000,1000)
turt.penup()
turt.goto(1000,1000)

# Seperate last game line from new terminal line -
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

wn.mainloop()
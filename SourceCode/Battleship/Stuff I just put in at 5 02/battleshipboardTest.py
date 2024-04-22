import turtle as t
from turtle import *

player1Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
player2Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

shipsList1 =   ['P','D','S','B','C' ]                              #list to hold ships
shipsList2 =   ['P','D','S','B','C' ]                              #list to hold ships
sizeList =     [ 2 , 3,  3,  4,  5  ]

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

gameOver = False

playerTurn = True
listOfTurts = []
turtRows = []
turtColumn = []
for turt in listOfTurts:
    turtRows.append((listOfTurts.index(turt)//10))
    turtColumn.append((listOfTurts.index(turt)%10))

colors = ['a','b','c','d']

turt = t.Turtle(shape='square')

def drawplayerBoard(turn,y):
    global player1Board, player1Board
    if turn == 1:
        board = player1Board
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
    # turt.onclick(gaming_w_Clicks)
    turt.penup()

# - LEFT SIDE -
def labLeft():
    # set position
    draw.penup()
    draw.setpos(-350,-100)
    draw.pendown()
    # write p1 letters
    draw.penup()
    draw.setpos(-417,420)
    draw.pendown()
    draw.write("  A     B     C    D    E    F    G    H    I     J",font=("Verdana", 12))
    # write p1 #'s
    draw.penup()
    draw.setpos(-440,30)
    draw.pendown()
    draw.write("10",font=("Verdana", 12))#1\n\n\n2\n\n\n3\n\n\n4\n\n\n5\n\n\n6\n\n\n7\n\n\n8\n\n\n\n9\n\n
    draw.penup()
    draw.setpos(-430,70)
    draw.pendown()
    draw.write("9",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,110)
    draw.pendown()
    draw.write("8",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,150)
    draw.pendown()
    draw.write("7",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,190)
    draw.pendown()
    draw.write("6",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,230)
    draw.pendown()
    draw.write("5",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,270)
    draw.pendown()
    draw.write("4",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,310)
    draw.pendown()
    draw.write("3",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,350)
    draw.pendown()
    draw.write("2",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,390)
    draw.pendown()
    draw.write("1",font=("Verdana", 12))
    # write p2 letters
    draw.penup()
    draw.setpos(-417,-30)
    draw.pendown()
    draw.write("  A     B     C     D     E     F     G     H     I     J",font=("Verdana", 12))
    # write p2 #'s
    draw.penup()
    draw.setpos(-430,-60)
    draw.pendown()
    draw.write("1",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-100)
    draw.pendown()
    draw.write("2",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-140)
    draw.pendown()
    draw.write("3",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-180)
    draw.pendown()
    draw.write("4",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-220)
    draw.pendown()
    draw.write("5",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-260)
    draw.pendown()
    draw.write("6",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-300)
    draw.pendown()
    draw.write("7",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-340)
    draw.pendown()
    draw.write("8",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-380)
    draw.pendown()
    draw.write("8",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-430,-420)
    draw.pendown()
    draw.write("9",font=("Verdana", 12))
    draw.penup()
    draw.setpos(-440,-460)
    draw.pendown()
    draw.write("10",font=("Verdana", 12))
    #player 1 label
    draw.penup()
    draw.setpos(-270,440)
    draw.pendown()
    draw.write("Player 1",font=("Verdana", 12, "bold"))
    #player 2 label
    draw.penup()
    draw.setpos(-270,-10)
    draw.pendown()
    draw.write("Player 2",font=("Verdana", 12, "bold"))

# - RIGHT SIDE -
#Method To Label Right Side -
def labRight():
    draw.penup()
    draw.setpos(150,410)
    draw.pendown()
    draw.write("- Directions -",font=("Verdana", 12, "bold"))
    draw.penup()
    draw.setpos(25,183)
    draw.pendown()
    draw.write("If you've played BattleShip before then you "
                "\nshould know how this works and can skip "
                "\nto How To Play. But if you don't then here's "
                "\nhow it works: "
                "\nYou will engage in battle with your oponent "
                "\nand take turns shooting at eachother's ships."
                "\nAfter you attack, your turn will be up and it "
                "\nwill be your opponents turn to attack you. "
                "\nThis will continue until smomeone has lost "
                "\nall 3 of their ships. "
                "\nFirst one to sink their enemies battleships "
                "\nis the WINNER!",font=("Verdana", 12))
    draw.penup()
    draw.setpos(140,130)
    draw.pendown()
    draw.write("- How to Play -",font=("Verdana", 12, "bold"))
    draw.penup()
    draw.setpos(25,-60)
    draw.pendown()
    draw.write("Now how you play this particular version, "
                "\nTake turns with your opponent, shooting at "
                "\nthe opposing board by clicking on a square "
                "\nof the enemy's team. "
                "\nThe game will end when one player has "
                "\ncompletly eliminated all of the other "
                "\nplayers ships.",font=("Verdana", 12))
    draw.penup()
#Set Keys/Buttons -


currPlaya = 1
def gaming_w_Clicks(x,y):
    global currPlaya, gameOver, playerTurn
    if playerTurn == True:
        if noShips(player2Board):
            draw.setpos(25,-100)
            draw.write("Player 1 wins",font=("Verdana", 15))
            draw.penup()
            draw.setpos(1000,1000)
            # break
        playerTurn = False

    elif playerTurn == False:
        if noShips(player1Board):
            draw.setpos(25,-100)
            draw.write("Player 2 wins",font=("Verdana", 15))
            draw.penup()
            draw.setpos(1000,1000)
            # break
        playerTurn = True

    for turt in listOfTurts:
        hit = 'red'
        miss = 'blue'
        if (turt.xcor()-25 < x < turt.xcor() +25) and (turt.ycor()-25 < y < turt.ycor() +25):
            color=turt.color()[1]
            

            # print(color)
            row = (listOfTurts.index(turt)//10)
            column = (listOfTurts.index(turt)%10)

            if row >= 10 and currPlaya == 2:
                currPlaya = 1
                row -= 10
                if player2Board[row][column] == "=":
                    turt.fillcolor(hit)
                    player2Board[row][column] = "X"
                    print(player2Board[row][column])

                elif player2Board[row][column] == " ":
                    turt.fillcolor(miss)
                    player2Board[row][column] = "O"
                    print(player2Board[row][column])
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

# def playerFireMiss(r,c,b):
#     if b[r][c]=="=":
#         b[r][c]='X'
#         return True
#     elif b[r][c]==" ":
#         b[r][c]='O'
#         return False

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
labLeft()
labRight()
draw.penup()
draw.goto(1000,1000)
turt.penup()
turt.goto(1000,1000)

# Seperate last game line from new terminal line -
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

# wn.onclick(gaming_w_Clicks)
wn.mainloop()
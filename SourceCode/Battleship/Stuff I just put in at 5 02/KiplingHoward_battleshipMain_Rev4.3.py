# Imports -
import random as rand
from random import randrange, sample 
from UIChecker import UIchecker 

# Game start - Print out controls when terminal runs
print('''

                <- BATTLE SHIP ->
- - - - - - - - - - - - - - - - - - - - - - - - -

                - Directions -

If you've played BattleShip before then you should 
know how this works and can skip to How To Play.
But if you don't then here's how it works:
You will engage in battle with your oponent and take 
turns shooting at eachother's
ships. After you attack, your turn will be up and it 
will be your opponents turn to attack you.
This will continue until smomeone has lost all 3 of 
their ships.
First one to sink their enemies battleships is the WINNER

                - How to Play -

Now how you play this particular version, you will
begin by typing the coordinates of where you want your ships to be at.
Ex: I want my ship to start at 1,1  (row,column).
After all ships have been placed the game will start.
you will choose where to attack the same way as you chose the 
position of your own ships
Ex: I want to attack at 5,1  (row,column).

- - - - - - - - - - - - - - - - - - - - - - - - -

                - Debug Controls -

Reset: R

- - - - - - - - - - - - - - - - - - - - - - - - -
''')

# Start game when user types in "start"
startInput = input("- Type 'start' to begin -\n\n> ")   #User input
startInput = startInput.lower()                                 #Make input lowercase

while startInput != "start":
    gameStart = False
    print("\n- Input Invalid -\n")
    startInput = input("        - Type 'start' to begin -\n\n> ")
    startInput = startInput.lower()

print("\n- - - - - - - - - - - - - - - - - - - - - - - - -")    #Seperate game controls screen from game boards

if startInput == "start":                                       #if the user typed in 'start'
    gameStart = True                                            # the bool = True


#Reset the game when user hits R
def reset():
    gameStart = False

# Board Lists -
player1Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

player2Board = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]




# Create 5 ships (3 ships for each player per game) -
shipsList1 =   ['P','D','S','B','C' ]                              #list to hold ships
shipsList2 =   ['P','D','S','B','C' ]                              #list to hold ships
sizeList =     [ 2 , 3,  3,  4,  5  ]                              #size of each ship

# Terminal Layout -
#prints the boards
def printPlayerBoard(b):                                 #Player 1 board layout -
    for r in range(len(b)):   
        for c in range(len(b[r])):   
            if c != (len(b[r])-1):
                print(b[r][c],end=" | ")
            else:
                print(b[r][c],end="\n")
        if r != (len(b)-1):
            print("-"*38)
    print()

print("\n\n            - Player 1 -")                    #Print out player 1 board -
printPlayerBoard(player1Board)                                           
print()
print("\n            - Player 2 -")                            #Print out player 2 board -
printPlayerBoard(player2Board)                                           
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

#sits upon eachother needs work
def printShipList(shiplist):
    out = ""
    for i in shiplist:
        if i == shiplist[len(shiplist)-1]:
            out += i
        else:
            out += (i+",")
    return out

def direction(direction,si_sh,board,row,column):    # direction(direction,sizeship,)
    if direction == 'R':    #if direction is right
        for i in range(si_sh):
            if board[row][column]==" ":
                board[row][column]='='
            column+=1   
        return True
    elif direction == 'L':    #if direction is left
        for i in range(si_sh):
            if board[row][column]==" ":
                board[row][column]='='
            column-=1   
        return True
    elif direction == 'U':    #if direction is up
        for i in range(si_sh):
            if board[row][column]==" ":
                board[row][column]='='
            row-=1  
        return True
    elif direction == 'D':    #if direction is down
        for i in range(si_sh):
            if board[row][column]==" ":
                board[row][column]='='
            row+=1  
        return True

#adds a ship on the board and makes it work with whatever direction the user chose
def addMark(shP,di,sizesh,r,c,b):   # direction(shipChoice,direction,row,column,playerboard)
        #if the space is blank, add that mark, tell the program we're good
        if shP == 'C':  #if ship is Carrier
            direction(di,sizesh,b,r,c)
        elif shP == 'B':    #if ship is Battleship
            direction(di,sizesh,b,r,c)
        elif shP == 'S':    #if ship is Submarine
            direction(di,sizesh,b,r,c)
        elif shP == 'D':    #if ship is Destroyer
            direction(di,sizesh,b,r,c)
        elif shP == 'P':    #if ship is Patrol Ship
            direction(di,sizesh,b,r,c)
        return False
#creates the 3 ships for Player 1
def shipMakerP1():  #makes the ship for Player 1
    # Place ships in boards -
    shipChoiceP1 = input("Player 1 - What ship do you want {}: ".format(printShipList(shipsList1))).upper()
    while not UIchecker.checkInput(shipsList1,shipChoiceP1):
        shipChoiceP1 = input("Player 1 - Not Valid, What ship do you want {}: ".format(printShipList(shipsList1))).upper()

    #Depending on what the Player picked will determine the size of the ship
    while True:
        if shipChoiceP1 in shipsList1:
            #Since 'C' was chosen, go to the index of ship['C'] in the sizelist (size[ship.index('C')])
            sizeOfShip = sizeList[shipsList1.index(shipChoiceP1)]     
            break
        # else:   #the user puts anything else other than P,D,S,B,C
        #     shipChoiceP1 = input("Player 1 - Not Correct, What ship do you want {}: ".format(printShipList(shipsList1))).upper()

    #if the row is not an integer it  will tell the user to put a number then re-ask them what row until they put a valid integer
    while True:
        try:
            row = int(input("What Row: "))-1
            if row > 10 or row < 0:
                row = int(input("Won't fit, What Row: "))-1
            else:
                break
        except ValueError:
            print("Has to be a number between 1-10: ")

    while True:
        try:
            column = int(input("What Column: "))-1  #asks the user what column to place the ship in
            if column < 0 or column > 10:
                column = int(input("Won't fit, What Column: "))-1
            else:
                break
        except ValueError:
            print("Has to be a number between 1-10: ")

    direction = input("What direction do you want the ship to go [Up,Down,Left,Right] (type U,D,L,R): ").upper()

    value = False
    while not value:
        if direction == 'R':
            while (row >= (10-sizeOfShip+1) and column >= (10-sizeOfShip+1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'L':
            while not (row >= (0+sizeOfShip-1) and column >= (0+sizeOfShip-1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'U':
            while (row >= (10-sizeOfShip+1) and column >= (10-sizeOfShip+1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'D':
            while not (row >= (0+sizeOfShip-1) and column >= (0+sizeOfShip-1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        else:
            direction = input("What direction do you want the ship to go [Up,Down,Left,Right] (type U,D,L,R): ").upper()

    # Place ships in boards -
    del shipsList1[shipsList1.index(shipChoiceP1)]
    ##Depending on what the Player picked will determine how much of the board gets taken up
 
    addMark(shipChoiceP1,direction,sizeOfShip,row,column,player1Board)      #actually prints the ship on the board

#creates the 3 ships for player 2
def shipMakerP2():
    # Place ships in boards -
    shipChoiceP2 = input("Player 2 - What ship do you want {}: ".format(printShipList(shipsList2))).upper()
    while not UIchecker.checkInput(shipsList2,shipChoiceP2):
        shipChoiceP2 = input("Player 2 - Not Valid, What ship do you want {}: ".format(printShipList(shipsList2))).upper()
    # print(shipChoiceP2)
    while True:
        if shipChoiceP2 in shipsList2:
            #Since 'C' was chosen, go to the index of ship['C'] in the sizelist (size[ship.index('C')])
            sizeOfShip = sizeList[shipsList2.index(shipChoiceP2)]     
            break
        else:   #the user puts anything else other than P,D,S,B,C
            shipChoiceP2 = input("Player 2 - Not Correct, What ship do you want {}: ".format(printShipList(shipsList2))).upper()

    while True:
        try:
            row = int(input("What Row: "))-1
            if row > 10 or row < 0:
                row = int(input("Won't fit, What Row: "))-1
            else:
                break
        except ValueError:
            print("Has to be a number between 1-10: ")

    while True:
        try:
            column = int(input("What Column: "))-1  #asks the user what column to place the ship in
            if column < 0 or column > 10:
                column = int(input("Won't fit, What Column: "))-1
            else:
                break
        except ValueError:
            print("Has to be a number between 1-10: ")

    direction = input("What direction do you want the ship to go [Up,Down,Left,Right] (type U,D,L,R): ").upper()

    value = False
    while not value:
        if direction == 'R':
            while (row >= (10-sizeOfShip+1) and column >= (10-sizeOfShip+1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'L':
            while not (row >= (0+sizeOfShip-1) and column >= (0+sizeOfShip-1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'U':
            while (row >= (10-sizeOfShip+1) and column >= (10-sizeOfShip+1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        elif direction == 'D':
            while not (row >= (0+sizeOfShip-1) and column >= (0+sizeOfShip-1)):
                row = int(input("Won't fit, What Row: "))-1
                column = int(input("Won't fit, What Column: "))-1
            value = True
        else:
            direction = input("What direction do you want the ship to go [Up,Down,Left,Right] (type U,D,L,R): ").upper()

    # Place ships in boards -
    del shipsList2[shipsList2.index(shipChoiceP2)]

    addMark(shipChoiceP2,direction,sizeOfShip,row,column,player2Board)

for i in range(3):
    shipMakerP1()
    printPlayerBoard(player1Board)     

for i in range(3):
    shipMakerP2()
    printPlayerBoard(player2Board)


#Re-Print Out Player Boards -
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n\n\n            - Player 1 -")
printPlayerBoard(player1Board)                                           
print()

print("\n            - Player 2 -")
printPlayerBoard(player2Board)                                           
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")


# REV 4:

# Create score-hit marks ('O' for misses, 'X' for hits) -
hit = "X"
miss = "0"

gameOver = False


playerTurn = True


# rowF = int(input("What Row F: "))-1
# columnF = int(input("What Column F: "))-1
def playerFireMiss(r,c,b):
    if b[r][c]=="=":
        b[r][c]='X'
        print("Hit")
        return True
    elif b[r][c]==" ":
        b[r][c]='O'
        print("Missed")
        return False

#checks if there are any ships on the board
def noShips(board):
    #if the board is full then it will be a tie
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "=":
                #there are still ships on the board
                return False
    #there are no more ships on the board and a player has won
    return True

while gameOver == False:
    
    if playerTurn == True:
        while True:
            try:
                rowF = int(input("Player 1 What Row do you want to attack: "))-1
                if rowF > 10 or rowF < 0:
                    rowF = int(input("Won't fit, What Row: "))-1
                else:
                    break
            except ValueError:
                print("Has to be a number between 1-10: ")
        
        
        while True:
            try:
                columnF = int(input("Player 1 What Column do you want to attack: "))-1
                if columnF > 10 or columnF < 0:
                    columnF = int(input("Won't fit, What Row: "))-1
                else:
                    break
            except ValueError:
                print("Has to be a number between 1-10: ")

        playerFireMiss(rowF,columnF,player2Board)

        print("\n- - - - - - - - - - - -Player 1 attacks- - - - - - - - - - - - -\n")
        print("\n- - - - - - - - - - - - Player 2 board- - - - - - - - - - - - -\n")
        printPlayerBoard(player2Board)
        if noShips(player2Board):
            print("Player 1 wins")
            break
        playerTurn = False

    elif playerTurn == False:

        while True:
            try:
                rowF = int(input("Player 2 What Row do you want to attack: "))-1
                if rowF > 10 or rowF < 0:
                    rowF = int(input("Won't fit, What Row: "))-1
                else:
                    break
            except ValueError:
                print("Has to be a number between 1-10: ")
        
        
        while True:
            try:
                columnF = int(input("Player 2 What Column do you want to attack: "))-1
                if columnF > 10 or columnF < 0:
                    columnF = int(input("Won't fit, What Row: "))-1
                else:
                    break
            except ValueError:
                print("Has to be a number between 1-10: ")
        playerFireMiss(rowF,columnF,player1Board)

        print("\n- - - - - - - - - - - -Player 2 attacks- - - - - - - - - - - - -\n")
        print("\n- - - - - - - - - - - - Player 1 board- - - - - - - - - - - - -\n")
        printPlayerBoard(player1Board)
        if noShips(player1Board):
            print("Player 2 wins")
            break
        playerTurn = True

# Seperate last game line from new terminal line -
print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
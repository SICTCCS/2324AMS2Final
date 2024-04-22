#class
class CheckInput:
    
    @staticmethod
    
    def getCorrectInput(ui,listOfAnswers,question):
        while not (ui in listOfAnswers):
            ui = (input(question))
        return ui

#defining
TitleCard="""
   _|_|_|  _|    _|  _|_|_|_|    _|_|_|  _|    _|  _|_|_|_|  _|_|_|      _|_|_|
 _|        _|    _|  _|        _|        _|  _|    _|        _|    _|  _|
 _|        _|_|_|_|  _|_|_|    _|        _|_|      _|_|_|    _|_|_|      _|_|
 _|        _|    _|  _|        _|        _|  _|    _|        _|    _|        _|
   _|_|_|  _|    _|  _|_|_|_|    _|_|_|  _|    _|  _|_|_|_|  _|    _|  _|_|_|
                                                                                      """
boardSpotList=[["r",".","r",".","r",".","r","."],[".","r",".","r",".","r",".","r"],["r",".","r",".","r",".","r","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".","b",".","b",".","b",".","b"],["b",".","b",".","b",".","b","."],[".","b",".","b",".","b",".","b"]]
ui=""
pieceCheck=0
row=0
column=0
endGame=0
playerTurn=0
turnFinish=0
blackOrRedCheck=0
winnerRedCheck=0
winnerBlackCheck=0
winnerColorCheck=0
pieceMoveCheckList=["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
#functions
def boardPrint():
    #prints updated board
    print(f"   1 2 3 4 5 6 7 8\n   _______________\na |{boardSpotList[0][0]} {boardSpotList[0][1]} {boardSpotList[0][2]} {boardSpotList[0][3]} {boardSpotList[0][4]} {boardSpotList[0][5]} {boardSpotList[0][6]} {boardSpotList[0][7]}\nb |{boardSpotList[1][0]} {boardSpotList[1][1]} {boardSpotList[1][2]} {boardSpotList[1][3]} {boardSpotList[1][4]} {boardSpotList[1][5]} {boardSpotList[1][6]} {boardSpotList[1][7]}\nc |{boardSpotList[2][0]} {boardSpotList[2][1]} {boardSpotList[2][2]} {boardSpotList[2][3]} {boardSpotList[2][4]} {boardSpotList[2][5]} {boardSpotList[2][6]} {boardSpotList[2][7]}\nd |{boardSpotList[3][0]} {boardSpotList[3][1]} {boardSpotList[3][2]} {boardSpotList[3][3]} {boardSpotList[3][4]} {boardSpotList[3][5]} {boardSpotList[3][6]} {boardSpotList[3][7]}\ne |{boardSpotList[4][0]} {boardSpotList[4][1]} {boardSpotList[4][2]} {boardSpotList[4][3]} {boardSpotList[4][4]} {boardSpotList[4][5]} {boardSpotList[4][6]} {boardSpotList[4][7]}\nf |{boardSpotList[5][0]} {boardSpotList[5][1]} {boardSpotList[5][2]} {boardSpotList[5][3]} {boardSpotList[5][4]} {boardSpotList[5][5]} {boardSpotList[5][6]} {boardSpotList[5][7]}\ng |{boardSpotList[6][0]} {boardSpotList[6][1]} {boardSpotList[6][2]} {boardSpotList[6][3]} {boardSpotList[6][4]} {boardSpotList[6][5]} {boardSpotList[6][6]} {boardSpotList[6][7]}\nh |{boardSpotList[7][0]} {boardSpotList[7][1]} {boardSpotList[7][2]} {boardSpotList[7][3]} {boardSpotList[7][4]} {boardSpotList[7][5]} {boardSpotList[7][6]} {boardSpotList[7][7]}")

def checkForPiece(location,player):
    global row
    global column
    global pieceCheck
    row=location[0]
    column=location[-1]
    #changes letter cor value to index value
    if row=="a":
        row=0
    elif row=="b":
        row=1
    elif row=="c":
        row=2
    elif row=="d":
        row=3
    elif row=="e":
        row=4
    elif row=="f":
        row=5
    elif row=="g":
        row=6
    elif row=="h":
        row=7
    column=int(column)-1
    #checks if cor selected is a piece that can be moved
    if player==0:
        if boardSpotList[row][column]=="b" or boardSpotList[row][column]=="B":
            pieceCheck=1
            return pieceCheck
    elif player==1:
        if boardSpotList[row][column]=="r" or boardSpotList[row][column]=="R":
            pieceCheck=1
            return pieceCheck

def movementHandler():
    global ui
    global boardSpotList
    global turnFinish
    global endGame
    global winnerRedCheck
    global winnerBlackCheck
    global winnerColorCheck
    #movement
    #checking for piece that is not a king
    if boardSpotList[row][column]=="r" or boardSpotList[row][column]=="b":
        #input for left and right movement
        ui=CheckInput.getCorrectInput(ui,["l","r"],"Would you like to move left or right? (Use 'l' or 'r'): ")
        #checking for red or black
        if boardSpotList[row][column]=="b":
            #try to move and if there is an index error, make player do a different input
            try:
                if ui=="l":
                    #jumping
                    if boardSpotList[row-1][column-1]=="r" or boardSpotList[row-1][column-1]=="R":
                        if boardSpotList[row-2][column-2]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column-1]="."
                            boardSpotList[row-2][column-2]="b"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    #moving forward
                    elif boardSpotList[row-1][column-1]==".":
                        boardSpotList[row][column]="."
                        boardSpotList[row-1][column-1]="b"
                    else:
                        print("That is not a possible move. Please try again.")
                        turnFinish=0
                elif ui=="r":
                    #jumping
                    if boardSpotList[row-1][column+1]=="r" or boardSpotList[row-1][column+1]=="R":
                        if boardSpotList[row-2][column+2]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column+1]="."
                            boardSpotList[row-2][column+2]="b"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    #moving forward
                    elif boardSpotList[row-1][column+1]==".":
                        boardSpotList[row][column]="."
                        boardSpotList[row-1][column+1]="b"
                    else:
                        print("That is not a possible move. Please try again.")
                        turnFinish=0
            #run this if there is an index error
            except IndexError:
                print("That is not a possible move. Please try again.")
                turnFinish=0
        #checking for red or black
        elif boardSpotList[row][column]=="r":
            #try to move and if there is an index error, make player do a different input
            try:
                if ui=="l":
                    #jumping
                    if boardSpotList[row+1][column-1]=="b" or boardSpotList[row+1][column-1]=="B":
                        if boardSpotList[row+2][column-2]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column-1]="."
                            boardSpotList[row+2][column-2]="r"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    #moving forward
                    elif boardSpotList[row+1][column-1]==".":
                        boardSpotList[row][column]="."
                        boardSpotList[row+1][column-1]="r"
                    else:
                        print("That is not a possible move. Please try again.")
                        turnFinish=0
                elif ui=="r":
                    #jumping
                    if boardSpotList[row+1][column+1]=="b" or boardSpotList[row-1][column+1]=="B":
                        if boardSpotList[row+2][column+2]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column+1]="."
                            boardSpotList[row+2][column+2]="r"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    #moving forward
                    elif boardSpotList[row+1][column+1]==".":
                        boardSpotList[row][column]="."
                        boardSpotList[row+1][column+1]="r"
                    else:
                        print("That is not a possible move. Please try again.")
                        turnFinish=0
            #run this if there is an index error
            except IndexError:
                print("That is not a possible move. Please try again.")
                turnFinish=0
    #check for king
    elif boardSpotList[row][column]=="R" or boardSpotList[row][column]=="B":
        #input for up or down king movement
        ui=CheckInput.getCorrectInput(ui,["u","d"],"Would you like to move up or down? (Use 'u' or 'd'): ")
        if ui=="u":
            #input for left and right movement
            ui=CheckInput.getCorrectInput(ui,["l","r"],"Would you like to move left or right? (Use 'l' or 'r'): ")
            if boardSpotList[row][column]=="B":
                #try to move and if there is an index error, make player do a different input
                try:
                    if ui=="l":
                        #jumping
                        if boardSpotList[row-1][column-1]=="r" or boardSpotList[row-1][column-1]=="R":
                            if boardSpotList[row-2][column-2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row-1][column-1]="."
                                boardSpotList[row-2][column-2]="B"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row-1][column-1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column-1]="B"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    elif ui=="r":
                        #jumping
                        if boardSpotList[row-1][column+1]=="r" or boardSpotList[row-1][column+1]=="R":
                            if boardSpotList[row-2][column+2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row-1][column+1]="."
                                boardSpotList[row-2][column+2]="B"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row-1][column+1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column+1]="B"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                #run this if there is an index error
                except IndexError:
                    print("That is not a possible move. Please try again.")
                    turnFinish=0
            elif boardSpotList[row][column]=="R":
                #try to move and if there is an index error, make player do a different input
                try:
                    if ui=="l":
                        #jumping
                        if boardSpotList[row-1][column-1]=="b" or boardSpotList[row-1][column-1]=="B":
                            if boardSpotList[row-2][column-2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row-1][column-1]="."
                                boardSpotList[row-2][column-2]="R"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row-1][column-1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column-1]="R"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    elif ui=="r":
                        #jumping
                        if boardSpotList[row-1][column+1]=="b" or boardSpotList[row-1][column+1]=="B":
                            if boardSpotList[row-2][column+2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row-1][column+1]="."
                                boardSpotList[row-2][column+2]="R"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row-1][column+1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row-1][column+1]="R"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                #run this if there is an index error
                except IndexError:
                    print("That is not a possible move. Please try again.")
                    turnFinish=0
        elif ui=="d":
            #input for left and right movement
            ui=CheckInput.getCorrectInput(ui,["l","r"],"Would you like to move left or right? (Use 'l' or 'r'): ")
            if boardSpotList[row][column]=="B":
                #try to move and if there is an index error, make player do a different input
                try:
                    if ui=="l":
                        #jumping
                        if boardSpotList[row+1][column-1]=="r" or boardSpotList[row+1][column-1]=="R":
                            if boardSpotList[row+2][column-2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row+1][column-1]="."
                                boardSpotList[row+2][column-2]="B"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row+1][column-1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column-1]="B"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    elif ui=="r":
                        #jumping
                        if boardSpotList[row+1][column+1]=="r" or boardSpotList[row+1][column+1]=="R":
                            if boardSpotList[row+2][column+2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row+1][column+1]="."
                                boardSpotList[row+2][column+2]="B"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row+1][column+1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column+1]="B"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                #run this if there is an index error
                except IndexError:
                    print("That is not a possible move. Please try again.")
                    turnFinish=0
            elif boardSpotList[row][column]=="R":
                #try to move and if there is an index error, make player do a different input
                try:
                    if ui=="l":
                        #jumping
                        if boardSpotList[row+1][column-1]=="b" or boardSpotList[row+1][column-1]=="B":
                            if boardSpotList[row+2][column-2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row+1][column-1]="."
                                boardSpotList[row+2][column-2]="R"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                        #moving forward
                        elif boardSpotList[row+1][column-1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column-1]="R"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                    elif ui=="r":
                        #jumping
                        if boardSpotList[row+1][column+1]=="b" or boardSpotList[row+1][column+1]=="B":
                            if boardSpotList[row+2][column+2]==".":
                                boardSpotList[row][column]="."
                                boardSpotList[row+1][column+1]="."
                                boardSpotList[row+2][column+2]="R"
                            else:
                                print("That is not a possible move. Please try again.")
                                turnFinish=0
                                #moving forward
                        elif boardSpotList[row+1][column+1]==".":
                            boardSpotList[row][column]="."
                            boardSpotList[row+1][column+1]="R"
                        else:
                            print("That is not a possible move. Please try again.")
                            turnFinish=0
                #run this if there is an index error
                except IndexError:
                    print("That is not a possible move. Please try again.")
                    turnFinish=0

    #changes pieces to kings when they reach other side
    for i in range(len(boardSpotList[0])):
        if boardSpotList[0][i]=="b":
            boardSpotList[0][i]="B"
        if boardSpotList[7][i]=="r":
            boardSpotList[7][i]="R"
    #checks for player pieces to decide winner
    for i in range(len(boardSpotList)):
        for j in range(len(boardSpotList[0])):
            if boardSpotList[i][j]=="r" or boardSpotList[i][j]=="R":
                winnerBlackCheck=winnerBlackCheck+1
                winnerColorCheck=1
                break
    for i in range(len(boardSpotList)):
        for j in range(len(boardSpotList[0])):
            if boardSpotList[i][j]=="b" or boardSpotList[i][j]=="B":
                winnerRedCheck=winnerRedCheck+1
                winnerColorCheck=0
                break
    #ends game if player isn't on board
    if winnerBlackCheck==0 or winnerRedCheck==0:
        endGame=1
    winnerRedCheck=0
    winnerBlackCheck=0
    ui=""


#---running code---
#program opening
while endGame!=1:
    print(TitleCard)
    ui=CheckInput.getCorrectInput(ui,["p","i"],"Type 'p' to play and 'i' to view the instructions: ")
    #instructions
    if ui=="i":
        ui=""
        print("\nBlack always goes first. On your turn, type the coordinate of the piece you would like to move (Ex: e5,h2,b4,etc.). The program will then ask if you would like to move the piece left or right and/or up or down depending on if the piece is a king or not. The rest of the game plays like normal checkers. Your goal is to capture all of the other player's pieces. Good luck!")
    #gameplay
    elif ui=="p":
        ui=""
        #switches turns
        while endGame!=1:
            turnFinish=0
            #player switcher using modulo
            playerTurn+=1
            if playerTurn%2!=0:
                while turnFinish==0:
                    ui=""
                    blackOrRedCheck=0
                    boardPrint()
                    print("Black's Turn!")
                    ui=CheckInput.getCorrectInput(ui,pieceMoveCheckList,"Which piece would you like to move? ")
                    #check if piece can be moved
                    pieceCheck=checkForPiece(ui,blackOrRedCheck)
                    if pieceCheck==1:
                        pieceCheck=0
                        turnFinish=1
                        movementHandler()
                    else:
                        print("\nThat's not a piece you can move. Please input the coordinates of a piece you can move.")
            else:
                while turnFinish==0:
                    ui=""
                    blackOrRedCheck=1
                    boardPrint()
                    print("Red's Turn!")
                    ui=CheckInput.getCorrectInput(ui,pieceMoveCheckList,"Which piece would you like to move? ")
                    #check if piece can be moved
                    pieceCheck=checkForPiece(ui,blackOrRedCheck)
                    if pieceCheck==1:
                        pieceCheck=0
                        turnFinish=1
                        movementHandler()
                    else:
                        print("\nThat's not a piece you can move. Please input the coordinates of a piece you can move.")

#winner text
if winnerColorCheck==0:
    print("""
                                                                                                        
    _|_|_|    _|                      _|            _|          _|  _|                      _|  _|  
    _|    _|  _|    _|_|_|    _|_|_|  _|  _|        _|          _|      _|_|_|      _|_|_|  _|  _|  
    _|_|_|    _|  _|    _|  _|        _|_|          _|    _|    _|  _|  _|    _|  _|_|      _|  _|  
    _|    _|  _|  _|    _|  _|        _|  _|          _|  _|  _|    _|  _|    _|      _|_|          
    _|_|_|    _|    _|_|_|    _|_|_|  _|    _|          _|  _|      _|  _|    _|  _|_|_|    _|  _|  
                                                                                                    
                                                                                                    
    """)
elif winnerColorCheck==1:
    print("""
                                                                                        
    _|_|_|                    _|      _|          _|  _|                      _|  _|  
    _|    _|    _|_|      _|_|_|      _|          _|      _|_|_|      _|_|_|  _|  _|  
    _|_|_|    _|_|_|_|  _|    _|      _|    _|    _|  _|  _|    _|  _|_|      _|  _|  
    _|    _|  _|        _|    _|        _|  _|  _|    _|  _|    _|      _|_|          
    _|    _|    _|_|_|    _|_|_|          _|  _|      _|  _|    _|  _|_|_|    _|  _|  
                                                                                    
                                                                                    
    """)
                
                

#Used to make ascii title: https://patorjk.com/software/taag/#p=display&f=Block&t=CHECKERS
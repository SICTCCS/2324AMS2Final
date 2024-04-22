#imports
import turtle as t
from functools import partial

#initialization
wn = t.Screen()
wn.bgcolor("sky blue")

#variable creation
whiteCheckers=[]
blackCheckers=[]
colorNumb,fwd=1,1
xCor=0
yCor=0
xTurt=0
yTurt=0
pieceColor=""
king=False
pieceInSpot=False

#create turtles
menuTurt=t.Turtle()
menuTurt.speed(0)
menuTurt.penup()
menuTurt.shape("square")
menuTurt.hideturtle()

option1=t.Turtle()
option1.speed(0)
option1.penup()
option1.shape("triangle")
option1.color("white")
option1.shapesize(1.5)
option1.hideturtle()

option2=t.Turtle()
option2.speed(0)
option2.penup()
option2.shape("triangle")
option2.color("white")
option2.shapesize(1.5)
option2.hideturtle()

option3=t.Turtle()
option3.speed(0)
option3.penup()
option3.shape("triangle")
option3.color("white")
option3.shapesize(1.5)
option3.hideturtle()

#checkers
w1=t.Turtle()
w1.speed(0)
w1.penup()
w1.shape("circle")
w1.color("white")
w1.shapesize(1.5)
w1.hideturtle()
whiteCheckers.append(w1)

w2=t.Turtle()
w2.speed(0)
w2.penup()
w2.shape("circle")
w2.color("white")
w2.shapesize(1.5)
w2.hideturtle()
whiteCheckers.append(w2)

w3=t.Turtle()
w3.speed(0)
w3.penup()
w3.shape("circle")
w3.color("white")
w3.shapesize(1.5)
w3.hideturtle()
whiteCheckers.append(w3)

w4=t.Turtle()
w4.speed(0)
w4.penup()
w4.shape("circle")
w4.color("white")
w4.shapesize(1.5)
w4.hideturtle()
whiteCheckers.append(w4)

w5=t.Turtle()
w5.speed(0)
w5.penup()
w5.shape("circle")
w5.color("white")
w5.shapesize(1.5)
w5.hideturtle()
whiteCheckers.append(w5)

w6=t.Turtle()
w6.speed(0)
w6.penup()
w6.shape("circle")
w6.color("white")
w6.shapesize(1.5)
w6.hideturtle()
whiteCheckers.append(w6)

w7=t.Turtle()
w7.speed(0)
w7.penup()
w7.shape("circle")
w7.color("white")
w7.shapesize(1.5)
w7.hideturtle()
whiteCheckers.append(w7)

w8=t.Turtle()
w8.speed(0)
w8.penup()
w8.shape("circle")
w8.color("white")
w8.shapesize(1.5)
w8.hideturtle()
whiteCheckers.append(w8)

w9=t.Turtle()
w9.speed(0)
w9.penup()
w9.shape("circle")
w9.color("white")
w9.shapesize(1.5)
w9.hideturtle()
whiteCheckers.append(w9)

w10=t.Turtle()
w10.speed(0)
w10.penup()
w10.shape("circle")
w10.color("white")
w10.shapesize(1.5)
w10.hideturtle()
whiteCheckers.append(w10)

w11=t.Turtle()
w11.speed(0)
w11.penup()
w11.shape("circle")
w11.color("white")
w11.shapesize(1.5)
w11.hideturtle()
whiteCheckers.append(w11)

w12=t.Turtle()
w12.speed(0)
w12.penup()
w12.shape("circle")
w12.color("white")
w12.shapesize(1.5)
w12.hideturtle()
whiteCheckers.append(w12)

b1=t.Turtle()
b1.speed(0)
b1.penup()
b1.shape("circle")
b1.color("black")
b1.shapesize(1.5)
b1.hideturtle()
blackCheckers.append(b1)

b2=t.Turtle()
b2.speed(0)
b2.penup()
b2.shape("circle")
b2.color("black")
b2.shapesize(1.5)
b2.hideturtle()
blackCheckers.append(b2)

b3=t.Turtle()
b3.speed(0)
b3.penup()
b3.shape("circle")
b3.color("black")
b3.shapesize(1.5)
b3.hideturtle()
blackCheckers.append(b3)

b4=t.Turtle()
b4.speed(0)
b4.penup()
b4.shape("circle")
b4.color("black")
b4.shapesize(1.5)
b4.hideturtle()
blackCheckers.append(b4)

b5=t.Turtle()
b5.speed(0)
b5.penup()
b5.shape("circle")
b5.color("black")
b5.shapesize(1.5)
b5.hideturtle()
blackCheckers.append(b5)

b6=t.Turtle()
b6.speed(0)
b6.penup()
b6.shape("circle")
b6.color("black")
b6.shapesize(1.5)
b6.hideturtle()
blackCheckers.append(b6)

b7=t.Turtle()
b7.speed(0)
b7.penup()
b7.shape("circle")
b7.color("black")
b7.shapesize(1.5)
b7.hideturtle()
blackCheckers.append(b7)

b8=t.Turtle()
b8.speed(0)
b8.penup()
b8.shape("circle")
b8.color("black")
b8.shapesize(1.5)
b8.hideturtle()
blackCheckers.append(b8)

b9=t.Turtle()
b9.speed(0)
b9.penup()
b9.shape("circle")
b9.color("black")
b9.shapesize(1.5)
b9.hideturtle()
blackCheckers.append(b9)

b10=t.Turtle()
b10.speed(0)
b10.penup()
b10.shape("circle")
b10.color("black")
b10.shapesize(1.5)
b10.hideturtle()
blackCheckers.append(b10)

b11=t.Turtle()
b11.speed(0)
b11.penup()
b11.shape("circle")
b11.color("black")
b11.shapesize(1.5)
b11.hideturtle()
blackCheckers.append(b11)

b12=t.Turtle()
b12.speed(0)
b12.penup()
b12.shape("circle")
b12.color("black")
b12.shapesize(1.5)
b12.hideturtle()
blackCheckers.append(b12)

#functions
def background1(): # **does not need to be touched** creates the checkerboard pattern for the background on the menu
    global colorNumb,fwd
    menuTurt.shapesize(5)
    menuTurt.setheading(0)
    #background creation
    menuTurt.goto(0,0)
    for x in range(8):
        for x in range(2):
            for x in range(fwd):
                if (colorNumb%2)==0:
                    menuTurt.color("red")
                else:
                    menuTurt.color("black")
                menuTurt.stamp()
                menuTurt.forward(100)
                colorNumb+=1
            menuTurt.right(90)
        fwd+=1
    colorNumb,fwd=1,1

def turtClear(): # clears and resets turtles
    option1.clear()
    option2.clear()
    option3.clear()
    menuTurt.hideturtle()
    option1.hideturtle()
    option2.hideturtle()
    option3.hideturtle()
    w1.hideturtle()
    w2.hideturtle()
    w3.hideturtle()
    w4.hideturtle()
    w5.hideturtle()
    w6.hideturtle()
    w7.hideturtle()
    w8.hideturtle()
    w9.hideturtle()
    w10.hideturtle()
    w11.hideturtle()
    w12.hideturtle()
    b1.hideturtle()
    b2.hideturtle()
    b3.hideturtle()
    b4.hideturtle()
    b5.hideturtle()
    b6.hideturtle()
    b7.hideturtle()
    b8.hideturtle()
    b9.hideturtle()
    b10.hideturtle()
    b11.hideturtle()
    b12.hideturtle()
    w1.pencolor("white")
    w2.pencolor("white")
    w3.pencolor("white")
    w4.pencolor("white")
    w5.pencolor("white")
    w6.pencolor("white")
    w7.pencolor("white")
    w8.pencolor("white")
    w9.pencolor("white")
    w10.pencolor("white")
    w11.pencolor("white")
    w12.pencolor("white")
    b1.pencolor("black")
    b2.pencolor("black")
    b3.pencolor("black")
    b4.pencolor("black")
    b5.pencolor("black")
    b6.pencolor("black")
    b7.pencolor("black")
    b8.pencolor("black")
    b9.pencolor("black")
    b10.pencolor("black")
    b11.pencolor("black")
    b12.pencolor("black")

def menuText(): # **does not need to be touched** writes menu text and created buttons
    #write title
    option1.goto(0,100)
    option1.write("Checkers",align="center", font=("Showcard Gothic", 80, "normal"))
    #play button title + button
    option1.goto(0,0)
    option1.write("Play",align="center", font=("Showcard Gothic", 30, "normal"))
    option1.goto(75,23)
    option1.showturtle()
    option1.onclick(gameModeFull)
    #instructions button title + button
    option2.goto(0,-100)
    option2.write("Instructions",align="center", font=("Showcard Gothic", 30, "normal"))
    option2.goto(165,-77)
    option2.showturtle()
    option2.onclick(instructionFull)
    #credits button title + button
    option3.goto(0,-200)
    option3.write("Credits",align="center", font=("Showcard Gothic", 30, "normal"))
    option3.goto(105,-177)
    option3.showturtle()
    option3.onclick(creditFull)
    
def instructionsText(): #writes instructions and adds buttons **instructions need to be written**
    #instructions title
    option1.goto(0,100)
    option1.write("Instructions:",align="center", font=("Showcard Gothic", 80, "normal"))
    #instructions
    option1.goto(0,0)
    option1.write("Lorem ipsum",align="center", font=("Showcard Gothic", 30, "normal"))
    #back + button
    option1.goto(0,-150)
    option1.write("Back",align="center", font=("Showcard Gothic", 30, "normal"))
    option1.goto(75,-127)
    option1.showturtle()
    option1.onclick(menuFull)
    
def creditsText(): # **does not need to be touched** writes credits and adds buttons
    #credits title
    option1.goto(0,100)
    option1.write("Made by:",align="center", font=("Showcard Gothic", 80, "normal"))
    #names
    option1.goto(0,0)
    option1.write("Jo and Bob",align="center", font=("Showcard Gothic", 30, "normal"))
    #back + button
    option1.goto(0,-100)
    option1.write("Back",align="center", font=("Showcard Gothic", 30, "normal"))
    option1.goto(70,-77)
    option1.showturtle()
    option1.onclick(menuFull)
    
def gameModeText(): # **does not need to be touched** writes game mode text and adds buttons
    #write title
    option1.goto(0,100)
    option1.write("Game Mode",align="center", font=("Showcard Gothic", 60, "normal"))
    #play button title + button
    option1.goto(0,0)
    option1.write("PvP",align="center", font=("Showcard Gothic", 30, "normal"))
    option1.goto(75,23)
    option1.showturtle()
    option1.onclick(pvpStart)
    #instructions button title + button
    option2.goto(0,-100)
    option2.write("PvC",align="center", font=("Showcard Gothic", 30, "normal"))
    option2.goto(75,-77)
    option2.showturtle()
    option2.onclick(pvcStart)
    #credits button title + button
    option3.goto(0,-200)
    option3.write("Back",align="center", font=("Showcard Gothic", 30, "normal"))
    option3.goto(75,-177)
    option3.showturtle()
    option3.onclick(menuFull)
    
def boardSetup(): # **does not need to be touched** created board pattern, places checkers, and adds button to main menu
    turtClear()
    menuTurt.clear()
    global colorNumb,fwd
    menuTurt.shapesize(2)
    #board creation 
    menuTurt.goto(-20,20)
    for x in range(7):
        for x in range(2):
            for x in range(fwd):
                if (colorNumb%2)==0:
                    menuTurt.color("red")
                else:
                    menuTurt.color("black")
                menuTurt.stamp()
                menuTurt.forward(40)
                colorNumb+=1
            menuTurt.right(90)
        fwd+=1
    for x in range(fwd):
        if (colorNumb%2)==0:
            menuTurt.color("red")
        else:
            menuTurt.color("black")
        menuTurt.stamp()
        menuTurt.forward(40)
        colorNumb+=1
    menuTurt.hideturtle()
    colorNumb,fwd=1,1
    #set checkers in place on board
    w1.goto(-100,140)
    w1.showturtle()
    w2.goto(-20,140)
    w2.showturtle()
    w3.goto(60,140)
    w3.showturtle()
    w4.goto(140,140)
    w4.showturtle()
    w5.goto(-140,100)
    w5.showturtle()
    w6.goto(-60,100)
    w6.showturtle()
    w7.goto(20,100)
    w7.showturtle()
    w8.goto(100,100)
    w8.showturtle()
    w9.goto(-100,60)
    w9.showturtle()
    w10.goto(-20,60)
    w10.showturtle()
    w11.goto(60,60)
    w11.showturtle()
    w12.goto(140,60)
    w12.showturtle()
    b1.goto(-140,-60)
    b1.showturtle()
    b2.goto(-60,-60)
    b2.showturtle()
    b3.goto(20,-60)
    b3.showturtle()
    b4.goto(100,-60)
    b4.showturtle()
    b5.goto(-100,-100)
    b5.showturtle()
    b6.goto(-20,-100)
    b6.showturtle()
    b7.goto(60,-100)
    b7.showturtle()
    b8.goto(140,-100)
    b8.showturtle()
    b9.goto(-140,-140)
    b9.showturtle()
    b10.goto(-60,-140)
    b10.showturtle()
    b11.goto(20,-140)
    b11.showturtle()
    b12.goto(100,-140)
    b12.showturtle()
    #main menu text + button
    option3.goto(60,-240)
    option3.write("Main Menu",align="center", font=("Showcard Gothic", 15, "normal"))
    option3.goto(130,-230)
    option3.showturtle()
    option3.onclick(gameToMenu)
    
def pieceMovement(t,x,y): # **does not need to be touched** keeps track of recent clicked turtle by saving information in variables
    global pieceColor,xTurt,yTurt,king
    option1.clear()
    option1.write("Checker selected. Click location to go to.",align="center", font=("Showcard Gothic", 15, "normal"))
    xTurt=t.xcor()
    yTurt=t.ycor()
    if t.fillcolor()=="white":
        pieceColor="white"
    elif t.fillcolor()=="black":
        pieceColor="black"
    if t.pencolor()=="lime":
        king=True
    else:
        king=False

def movementLogic(x,y): # **needs code added for king movement** takes screen click and previously clicked turtle info to decide if clicked location is a possible move
    global xCor,yCor,pieceColor,king,xTurt,yTurt,pieceInSpot
    #limits clicks to be inside board
    if x >= -160 and x <= 160:
        if y >= -160 and y <= 160:
            xCor,yCor=x,y
            #king movement
            if king==True:
                pass
            #white movement
            elif pieceColor=="white":
                if yCor <= yTurt-20 and yCor >= yTurt-60:
                    if xCor <= xTurt-20 and xCor >= xTurt-60:
                        # white left movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt-40 and checker.ycor()==yTurt-40:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt-40 and checker.ycor()==yTurt-40:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in whiteCheckers:
                                if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                    #successful move: white left single
                                    checker.goto(checker.xcor()-40,checker.ycor()-40)
                                    if checker.ycor()==-140:
                                        checker.pencolor("lime")
                                    blackTurn()
                    elif xCor >= xTurt+20 and xCor <= xTurt+60:
                        # white right movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt+40 and checker.ycor()==yTurt-40:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt+40 and checker.ycor()==yTurt-40:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in whiteCheckers:
                                if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                    #successful move: white right single
                                    checker.goto(checker.xcor()+40,checker.ycor()-40)
                                    if checker.ycor()==-140:
                                        checker.pencolor("lime")
                                    blackTurn()
                elif yCor <= yTurt-60 and yCor >= yTurt-100:
                    if xCor <= xTurt-60 and xCor >= xTurt-100:
                        # white left jump movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt-80 and checker.ycor()==yTurt-80:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt-80 and checker.ycor()==yTurt-80:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in whiteCheckers:
                                if checker.xcor()==xTurt-40 and checker.ycor()==yTurt-40:
                                    pieceInSpot=True
                            if pieceInSpot==False:
                                for checker in blackCheckers:
                                    if checker.xcor()==xTurt-40 and checker.ycor()==yTurt-40:
                                        checker.hideturtle()
                                        checker.goto(1000,1000)
                                        pieceInSpot=True
                                if pieceInSpot==True:
                                    for checker in whiteCheckers:
                                        if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                            #successful move: white left jump
                                            checker.goto(checker.xcor()-80,checker.ycor()-80)
                                            if checker.ycor()==-140:
                                                checker.pencolor("lime")
                                            blackTurn()
                                else:
                                    option1.clear()
                                    option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            else:
                                option1.clear()
                                option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                                pieceInSpot=False
                    elif xCor >= xTurt+60 and xCor <= xTurt+100:
                        # white right jump movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt+80 and checker.ycor()==yTurt-80:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt+80 and checker.ycor()==yTurt-80:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in whiteCheckers:
                                if checker.xcor()==xTurt+40 and checker.ycor()==yTurt-40:
                                    pieceInSpot=True
                            if pieceInSpot==False:
                                for checker in blackCheckers:
                                    if checker.xcor()==xTurt+40 and checker.ycor()==yTurt-40:
                                        checker.hideturtle()
                                        checker.goto(1000,1000)
                                        pieceInSpot=True
                                if pieceInSpot==True:
                                    for checker in whiteCheckers:
                                        if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                            #successful move: white right jump
                                            checker.goto(checker.xcor()+80,checker.ycor()-80)
                                            if checker.ycor()==-140:
                                                checker.pencolor("lime")
                                            blackTurn()
                                else:
                                    option1.clear()
                                    option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            else:
                                option1.clear()
                                option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                                pieceInSpot=False
            #black movement
            elif pieceColor=="black":
                if yCor >= yTurt+20 and yCor <= yTurt+60:
                    if xCor <= xTurt-20 and xCor >= xTurt-60:
                        # black left movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt-40 and checker.ycor()==yTurt+40:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt-40 and checker.ycor()==yTurt+40:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in blackCheckers:
                                if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                    #successful move: black left single
                                    checker.goto(checker.xcor()-40,checker.ycor()+40)
                                    if checker.ycor()==140:
                                        checker.pencolor("lime")
                                    whiteTurn()
                    elif xCor >= xTurt+20 and xCor <= xTurt+60:
                        # black right movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt+40 and checker.ycor()==yTurt+40:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt+40 and checker.ycor()==yTurt+40:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in blackCheckers:
                                if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                    #successful move: black right single
                                    checker.goto(checker.xcor()+40,checker.ycor()+40)
                                    if checker.ycor()==140:
                                        checker.pencolor("lime")
                                    whiteTurn()
                elif yCor >= yTurt+60 and yCor <= yTurt+100:
                    if xCor <= xTurt-60 and xCor >= xTurt-100:
                        # black left jump movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt-80 and checker.ycor()==yTurt+80:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt-80 and checker.ycor()==yTurt+80:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in blackCheckers:
                                if checker.xcor()==xTurt-40 and checker.ycor()==yTurt+40:
                                    pieceInSpot=True
                            if pieceInSpot==False:
                                for checker in whiteCheckers:
                                    if checker.xcor()==xTurt-40 and checker.ycor()==yTurt+40:
                                        checker.hideturtle()
                                        checker.goto(1000,1000)
                                        pieceInSpot=True
                                if pieceInSpot==True:
                                    for checker in blackCheckers:
                                        if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                            #successful move: black left jump
                                            checker.goto(checker.xcor()-80,checker.ycor()+80)
                                            if checker.ycor()==140:
                                                checker.pencolor("lime")
                                            whiteTurn()
                                else:
                                    option1.clear()
                                    option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            else:
                                option1.clear()
                                option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                                pieceInSpot=False
                    elif xCor >= xTurt+60 and xCor <= xTurt+100:
                        # black right jump movement logic
                        for checker in whiteCheckers:
                            if checker.xcor()==xTurt+80 and checker.ycor()==yTurt+80:
                                pieceInSpot=True
                        for checker in blackCheckers:
                            if checker.xcor()==xTurt+80 and checker.ycor()==yTurt+80:
                                pieceInSpot=True
                        if pieceInSpot==True:
                            option1.clear()
                            option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            pieceInSpot=False
                        else:
                            for checker in blackCheckers:
                                if checker.xcor()==xTurt+40 and checker.ycor()==yTurt+40:
                                    pieceInSpot=True
                            if pieceInSpot==False:
                                for checker in whiteCheckers:
                                    if checker.xcor()==xTurt+40 and checker.ycor()==yTurt+40:
                                        checker.hideturtle()
                                        checker.goto(1000,1000)
                                        pieceInSpot=True
                                if pieceInSpot==True:
                                    for checker in blackCheckers:
                                        if checker.xcor()==xTurt and checker.ycor()==yTurt:
                                            #successful move: black right jump
                                            checker.goto(checker.xcor()+80,checker.ycor()+80)
                                            if checker.ycor()==140:
                                                checker.pencolor("lime")
                                            whiteTurn()
                                else:
                                    option1.clear()
                                    option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                            else:
                                option1.clear()
                                option1.write("Not a possible move! Please try again.",align="center", font=("Showcard Gothic", 15, "normal"))
                                pieceInSpot=False
            
def menuFull(x,y): # **does not need to be touched** clears the text and prints menu text + buttons
    turtClear()
    menuText()
    
def creditFull(x,y): # **does not need to be touched** clears the text and prints credits text + buttons
    turtClear()
    creditsText()
    
def instructionFull(x,y): # **does not need to be touched** clears the text and prints instructions text + buttons
    turtClear()
    instructionsText()
    
def gameModeFull(x,y): # **does not need to be touched** clears the text and prints game mode text + buttons
    turtClear()
    gameModeText()
    
def gameToMenu(x,y): # **does not need to be touched** clears game screen, resets variables, and makes main menu screen
    varReset()
    turtClear()
    menuTurt.clear()
    background1()
    menuText()
    
def pvpStart(x,y): # **does not need to be touched** sets up board and set onclick functions for checkers
    boardSetup()
    option1.goto(0,-200)
    option1.write("Click a checker to make the first move",align="center", font=("Showcard Gothic", 15, "normal"))
    w1.onclick(partial(pieceMovement,w1))
    w2.onclick(partial(pieceMovement,w2))
    w3.onclick(partial(pieceMovement,w3))
    w4.onclick(partial(pieceMovement,w4))
    w5.onclick(partial(pieceMovement,w5))
    w6.onclick(partial(pieceMovement,w6))
    w7.onclick(partial(pieceMovement,w7))
    w8.onclick(partial(pieceMovement,w8))
    w9.onclick(partial(pieceMovement,w9))
    w10.onclick(partial(pieceMovement,w10))
    w11.onclick(partial(pieceMovement,w11))
    w12.onclick(partial(pieceMovement,w12))
    b1.onclick(partial(pieceMovement,b1))
    b2.onclick(partial(pieceMovement,b2))
    b3.onclick(partial(pieceMovement,b3))
    b4.onclick(partial(pieceMovement,b4))
    b5.onclick(partial(pieceMovement,b5))
    b6.onclick(partial(pieceMovement,b6))
    b7.onclick(partial(pieceMovement,b7))
    b8.onclick(partial(pieceMovement,b8))
    b9.onclick(partial(pieceMovement,b9))
    b10.onclick(partial(pieceMovement,b10))
    b11.onclick(partial(pieceMovement,b11))
    b12.onclick(partial(pieceMovement,b12))

def pvcStart(x,y): # **needs a lot of work** supposed to set up pvc 
    # no function right now
    boardSetup()
    option1.goto(0,-200)
    option1.write("Click a black checker to make the first move",align="center", font=("Showcard Gothic", 15, "normal"))
    
def whiteTurn(): # **does not need to be touched** changes turn to white color
    varReset()
    w1.onclick(partial(pieceMovement,w1))
    w2.onclick(partial(pieceMovement,w2))
    w3.onclick(partial(pieceMovement,w3))
    w4.onclick(partial(pieceMovement,w4))
    w5.onclick(partial(pieceMovement,w5))
    w6.onclick(partial(pieceMovement,w6))
    w7.onclick(partial(pieceMovement,w7))
    w8.onclick(partial(pieceMovement,w8))
    w9.onclick(partial(pieceMovement,w9))
    w10.onclick(partial(pieceMovement,w10))
    w11.onclick(partial(pieceMovement,w11))
    w12.onclick(partial(pieceMovement,w12))
    b1.onclick(wrongColor)
    b2.onclick(wrongColor)
    b3.onclick(wrongColor)
    b4.onclick(wrongColor)
    b5.onclick(wrongColor)
    b6.onclick(wrongColor)
    b7.onclick(wrongColor)
    b8.onclick(wrongColor)
    b9.onclick(wrongColor)
    b10.onclick(wrongColor)
    b11.onclick(wrongColor)
    b12.onclick(wrongColor)
    option1.clear()
    option1.write("White's turn!",align="center", font=("Showcard Gothic", 15, "normal"))

def blackTurn(): # **does not need to be touched** changes turn to black color
    varReset()
    w1.onclick(wrongColor)
    w2.onclick(wrongColor)
    w3.onclick(wrongColor)
    w4.onclick(wrongColor)
    w5.onclick(wrongColor)
    w6.onclick(wrongColor)
    w7.onclick(wrongColor)
    w8.onclick(wrongColor)
    w9.onclick(wrongColor)
    w10.onclick(wrongColor)
    w11.onclick(wrongColor)
    w12.onclick(wrongColor)
    b1.onclick(partial(pieceMovement,b1))
    b2.onclick(partial(pieceMovement,b2))
    b3.onclick(partial(pieceMovement,b3))
    b4.onclick(partial(pieceMovement,b4))
    b5.onclick(partial(pieceMovement,b5))
    b6.onclick(partial(pieceMovement,b6))
    b7.onclick(partial(pieceMovement,b7))
    b8.onclick(partial(pieceMovement,b8))
    b9.onclick(partial(pieceMovement,b9))
    b10.onclick(partial(pieceMovement,b10))
    b11.onclick(partial(pieceMovement,b11))
    b12.onclick(partial(pieceMovement,b12))
    option1.clear()
    option1.write("Black's turn!",align="center", font=("Showcard Gothic", 15, "normal"))

def wrongColor(x,y): # **does not need to be touched** prints wrong color if wrong color is clicked
    option1.clear()
    option1.write("Wrong color! Select a checker of the other color.",align="center", font=("Showcard Gothic", 12, "normal"))
    
def varReset(): # **does not need to be touched** resets all game involved variables
    global xCor,yCor,xTurt,yTurt,pieceColor,king,pieceInSpot
    xCor=0
    yCor=0
    xTurt=0
    yTurt=0
    pieceColor=""
    king=False
    pieceInSpot=False
    
#running code
background1()
menuText()

wn.onscreenclick(movementLogic)


wn.mainloop()
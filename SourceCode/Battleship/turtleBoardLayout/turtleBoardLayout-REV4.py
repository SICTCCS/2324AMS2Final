
#Imports -
import turtle as t

#Window Config -
wn = t.Screen()
wn.setup(width = 800, height = 900)
wn.title("Battleship")

#Drawing Turtle Config -
draw = t.Turtle()
draw.speed("fastest")
draw.penup()
draw.setpos(-350,-60)
draw.hideturtle()



#Testing Turtles -
b2 = t.Turtle()
b2.speed("fastest")
b2.color("red")
b2.shape("square")
b2.penup()
b2.setpos(-297,328)

c2 = t.Turtle()
c2.speed("fastest")
c2.color("orange")
c2.shape("square")
c2.penup()
c2.setpos(-262,328)

d2 = t.Turtle()
d2.speed("fastest")
d2.color("gold")
d2.shape("square")
d2.penup()
d2.setpos(-227,328)

f4 = t.Turtle()
f4.speed("fastest")
f4.color("green")
f4.shape("square")
f4.penup()
f4.setpos(-157,258)

f5 = t.Turtle()
f5.speed("fastest")
f5.color("blue")
f5.shape("square")
f5.penup()
f5.setpos(-157,223)

f6 = t.Turtle()
f6.speed("fastest")
f6.color("purple")
f6.shape("square")
f6.penup()
f6.setpos(-157,188)



# - LEFT SIDE -

# method to draw y-axis lines
def drawy(val):
      
    # line
    draw.forward(350)
      
    # set position
    draw.up()
    draw.setpos(-350,380)
    draw.down()

    # another line
    draw.backward(350)
      
    # set position again
    draw.up()
    draw.setpos(val-350,30)
    draw.down()

def drawy2(val):
      
    # line
    draw.forward(350)
      
    # set position
    draw.up()
    draw.setpos(-350,-50)
    draw.down()

    # another line
    draw.backward(350)
      
    # set position again
    draw.up()
    draw.penup()
    draw.setpos(val-350,-400)
    draw.pendown()
    draw.down()
      
# method to draw x-axis lines
def drawx(val):
      
    # line
    draw.forward(350)
      
    # set position
    draw.up()
    draw.setpos(-450,val)
    draw.down()
      
    # another line
    draw.backward(350)
      
    # set position again
    draw.up()
    draw.setpos(-350,val-5)
    draw.down()

def drawx2(val):
      
    # line
    draw.forward(350)
      
    # set position
    draw.up()
    draw.setpos(-450,-400)
    draw.down()
     
    # another line
    draw.backward(350)
      
    # set position again
    draw.up()
    draw.setpos(-350,val-400)
    draw.down()
    
# method to label the graph grid
def labLeft():
      
    # set position
    draw.penup()
    draw.setpos(-350,-100)
    draw.pendown()
      
    # write p1 letters
    draw.penup()
    draw.setpos(-350,380)
    draw.pendown()
    draw.write("  A    B    C    D    E    F    G    H    I     J",font=("Verdana", 12))

    # write p2 letters
    draw.penup()
    draw.setpos(-350,380)
    draw.pendown()
    draw.write("  A    B    C    D    E    F    G    H    I     J",font=("Verdana", 12))
      
    # write p1 #'s
    draw.penup()
    draw.setpos(-370,33)
    draw.pendown()
    draw.write("1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n10  ",font=("Verdana", 12))

    # write p2 letters
    draw.penup()
    draw.setpos(-350,-50)
    draw.pendown()
    draw.write("  A    B    C    D    E    F    G    H    I     J",font=("Verdana", 12))

    # write p2 #'s
    draw.penup()
    draw.setpos(-370,-400)
    draw.pendown()
    draw.write("1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n10  ",font=("Verdana", 12))

    #player 1 label
    draw.penup()
    draw.setpos(-210,410)
    draw.pendown()
    draw.write("Player 1",font=("Verdana", 12, "bold"))

    #player 2 label
    draw.penup()
    draw.setpos(-210,-20)
    draw.pendown()
    draw.write("Player 2",font=("Verdana", 12, "bold"))
  
# set turtle features
draw.left(90)
  
# y lines
for i in range(10):
    drawy(35*(i+1))

for i in range(11):
    drawy2(35*(i+1))
  
# set position for x lines
draw.right(90)
draw.up()
draw.setpos(-350,380)
draw.down()
  
# x lines
for i in range(11):
    drawx(35*(i+1))

draw.penup()
draw.setpos(-350,-400)
draw.pendown()
for i in range(11):
    drawx2(35*(i+1))
  
# labeling
labLeft()



# - TOP RIGHT SIDE -

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
                "\nyou will begin by typing the coordinates of "  
                "\nwhere you want your ships to be at. "
                "\nEx: I want my ship to start at 1,1 "
                "\n(row,column). "
                "\nAfter all ships have been placed the game "
                "\nwill start. you will choose where to attack "
                "\nthe same way as you chose the position of "
                "\nyour own ships. "
                "\nEx: I want to attack at 5,1  (row,column).",font=("Verdana", 12))

#Call Functions -
labRight()



# - BOTTOM RIGHT SIDE -

#User Input Turtles -
draw.penup()
draw.goto(150,-140)
draw.write("- Player 1 -",font=("Verdana", 12, "bold"))

def ATurtle():
    A = t.Turtle()
    A.speed("fastest")
    A.penup()

    Apng = "A.gif"
    wn.addshape(Apng)
    A.shape(Apng)

    A.setpos(25,-160)

    def AClicked(x,y):
        print("A was clicked")

    A.onclick(AClicked)

def BTurtle():
    B = t.Turtle()
    B.speed("fastest")
    B.penup()

    Bpng = "B.gif"
    wn.addshape(Bpng)
    B.shape(Bpng)

    B.setpos(55,-159)

    def BClicked(x,y):
        print("B was clicked")

    B.onclick(BClicked)

def CTurtle():
    C = t.Turtle()
    C.speed("fastest")
    C.penup()

    Cpng = "C.gif"
    wn.addshape(Cpng)
    C.shape(Cpng)

    C.setpos(85,-159)

    def CClicked(x,y):
        print("C was clicked")

    C.onclick(CClicked)

def DTurtle():
    D = t.Turtle()
    D.speed("fastest")
    D.penup()

    Dpng = "D.gif"
    wn.addshape(Dpng)
    D.shape(Dpng)

    D.setpos(115,-159)

    def DClicked(x,y):
        print("D was clicked")

    D.onclick(DClicked)

def ETurtle():
    E = t.Turtle()
    E.speed("fastest")
    E.penup()

    Epng = "E.gif"
    wn.addshape(Epng)
    E.shape(Epng)

    E.setpos(145,-159)

    def EClicked(E,y):
        print("E was clicked")

    E.onclick(EClicked)

def FTurtle():
    F = t.Turtle()
    F.speed("fastest")
    F.penup()

    Fpng = "F.gif"
    wn.addshape(Fpng)
    F.shape(Fpng)

    F.setpos(175,-159)

    def FClicked(F,y):
        print("F was clicked")

    F.onclick(FClicked)

'''
def XTurtle():
    X = t.Turtle()
    X.speed("fastest")
    X.penup()

    #Xpng = "X.gif"
    #wn.addshape(Xpng)
    #X.shape(Xpng)

    X.setpos(55,-159)
    X.write("X",font=("Verdana", 12, "bold"))
    X.hideturtle()

    def XClicked(x,y):
        print("X was clicked")

    X.onclick(XClicked)
'''


#Turtles -
ATurtle()
BTurtle()
CTurtle()
DTurtle()
ETurtle()
FTurtle()
#GTurtle()
#HTurtle()
#ITurtle()
#JTurtle()


wn.mainloop()


#Sources -
'''
https://www.geeksforgeeks.org/draw-graph-grid-using-turtle-in-python/
'''
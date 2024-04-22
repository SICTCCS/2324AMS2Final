#imports
import turtle as t
import random
import time
from BoardTurtles import BoardTurtles

wn = t.Screen()
wn.setup(width = 600,height = 600)


#Window Config -
wn = t.Screen()
wn.setup(width = 800, height = 900)
wn.title("Battleship")
#Drawing Turtle Config -
draw = t.Turtle()
draw.speed("fastest")
draw.penup()
draw.setpos(-350,-60)
#Testing Turtles -
BoardTurtles()

# - LEFT SIDE -
# method to draw y-axis lines
'''def drawy(val):
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
# method to label the graph grid'''
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
'''for i in range(10):
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
    drawx2(35*(i+1))'''
# labeling
labLeft()
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
#Set Keys/Buttons -
#Call Functions -
labRight()
# hide draw
draw.hideturtle()
wn.mainloop()
#Sources -
# 
# https://www.geeksforgeeks.org/draw-graph-grid-using-turtle-in-python/
#

wn.mainloop()

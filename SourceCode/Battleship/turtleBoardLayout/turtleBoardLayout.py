
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
draw.setpos(-350,-100)


# method to draw y-axis lines
def drawy(val):
      
    # line
    draw.forward(350)
      
    # set position
    draw.up()
    draw.setpos(-350,340)
    draw.down()

    # another line
    draw.backward(350)
      
    # set position again
    draw.up()
    draw.setpos(val-350,-10)
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
    draw.setpos(-350,val-10)
    draw.down()
      
# method to label the graph grid
def lab():
      
    # set position
    draw.penup()
    draw.setpos(-350,-100)
    draw.pendown()
      
    # set position again
    draw.penup()
    draw.setpos(-350,340)
    draw.pendown()
      
    # write x
    draw.write("  A    B    C    D    E    F    G    H    I     J",font=("Verdana", 12))
      
    # set position again
    draw.penup()
    draw.setpos(-370,-7)
    draw.pendown()
      
    # write y
    draw.write("1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n10  ",font=("Verdana", 12))

    #player 1 label
    draw.penup()
    draw.setpos(-210,370)
    draw.pendown()
    draw.write("Player 1",font=("Verdana", 12, "bold"))

    #player 2 label
    draw.penup()
    draw.setpos(-210,-60)
    draw.pendown()
    draw.write("Player 2",font=("Verdana", 12, "bold"))
  
# set turtle features
draw.left(90)
  
# y lines
for i in range(11):
    drawy(35*(i+1))
  
# set position for x lines
draw.right(90)
draw.up()
draw.setpos(-350,-10)
draw.down()
  
# x lines
for i in range(11):
    drawx(35*(i+1))
  
# labeling
lab()
  
# hide the drawe
draw.hideturtle()




wn.mainloop()


#Sources -
'''
https://www.geeksforgeeks.org/draw-graph-grid-using-turtle-in-python/
'''
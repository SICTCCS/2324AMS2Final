class Directions_Text:

    @staticmethod
    # - LEFT SIDE -
    def labLeft(draw):
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
    
    @staticmethod
    # - RIGHT SIDE -
    #Method To Label Right Side -
    def labRight(draw):
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

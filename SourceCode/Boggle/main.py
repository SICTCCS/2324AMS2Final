import turtle as t
import random
titleSetup = ("Arial",50,"normal")
fontSetup = ("Arial",30,"normal")
aimage = "Aboggle.gif"
bimage = "Bboggle.gif"
cimage = "Cboggle.gif"
dimage = "Dboggle.gif"
eimage = "Eboggle.gif"
fimage = "Fboggle.gif"
gimage = "Gboggle.gif"
himage = "Hboggle.gif"
iimage = "Iboggle.gif"
jimage = "Jboggle.gif"
kimage = "Kboggle.gif"
limage = "Lboggle.gif"
mimage = "Mboggle.gif"
nimage = "Nboggle.gif"
oimage = "Oboggle.gif"
pimage = "Pboggle.gif"
qimage = "Qboggle.gif"
rimage = "Rboggle.gif"
simage = "Sboggle.gif"
timage = "Tboggle.gif"
uimage = "Uboggle.gif"
vimage = "Vboggle.gif"
wimage = "Wboggle.gif"
ximage = "Xboggle.gif"
yimage = "Yboggle.gif"
zimage = "Zboggle.gif"

letters = [aimage,bimage,cimage,dimage,eimage,fimage,gimage,himage,iimage,jimage,kimage,limage,mimage,nimage,oimage,pimage,qimage,rimage,simage,timage,uimage,vimage,wimage,ximage,yimage,zimage]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bo = []
row = [] 
usedWords = []
strikes = 0

turn = 1
player1points = 0
player2points = 0

x1y1 = t.Turtle()
x2y1 = t.Turtle()
x3y1 = t.Turtle()
x4y1 = t.Turtle()
x1y2 = t.Turtle()
x2y2 = t.Turtle()
x3y2 = t.Turtle()
x4y2 = t.Turtle()
x1y3 = t.Turtle()
x2y3 = t.Turtle()
x3y3 = t.Turtle()
x4y3 = t.Turtle()
x1y4 = t.Turtle()
x2y4 = t.Turtle()
x3y4 = t.Turtle()
x4y4 = t.Turtle()
submit = t.Turtle()
scorer = t.Turtle()
reset = t.Turtle()

points = 0

wn = t.Screen()
wn.setup(width=600,height=600)
wn.title("Boggle")
wn.bgcolor("#6F8FAF")

for i in range(len(letters)):
    wn.addshape(letters[i])

wn.addshape("submitbutton.gif")
wn.addshape('resetbutton.gif')
wn.addshape("board.gif")

writer = t.Turtle()

pvps = t.Turtle()
pvps.shape("square")
pvps.penup()
pvps.goto(-50,25)
pvps.color("black")
pvps.write("PVP",font=fontSetup)
pvps.color("white")
pvps.goto(-75,50)

pvcs = t.Turtle()
pvcs.shape("square")
pvcs.penup()
pvcs.goto(-50,-50)
pvcs.color("black")
pvcs.write("PVC",font=fontSetup)
pvcs.color("white")
pvcs.goto(-75,-25)


tutorial = t.Turtle()
tutorial.shape("square")
tutorial.penup()
tutorial.goto(-50,-110)
tutorial.color("black")
tutorial.write("DIRECTIONS",font=fontSetup)
tutorial.color("white")
tutorial.goto(-75,-90)

credits = t.Turtle()
credits.shape("square")
credits.penup()
credits.goto(-50,-175)
credits.color("black")
credits.write("CREDITS",font=fontSetup)
credits.color("white")
credits.goto(-75,-150)

b = t.Turtle()
b.shape(letters[1])
b.penup()
b.setpos(-250,150)

o = t.Turtle()
o.shape(oimage)
o.penup()
o.setpos(-150,150)

o = t.Turtle()
o.shape(oimage)
o.penup()
o.setpos(-50,150)

g = t.Turtle()
g.shape(gimage)
g.penup()
g.setpos(50,150)

l = t.Turtle()
l.shape(limage)
l.penup()
l.setpos(150,150)

e = t.Turtle()
e.shape(eimage)
e.penup()
e.setpos(250,150)




with open("words.txt") as f:
    word_list = [word.strip().lower() for word in f]

def is_valid_word(word):
    return word in word_list

def credit(x,y):
    wn.clearscreen()
    wn.bgcolor("#6F8FAF")
    cred = t.Turtle()
    cred.color("Black")
    cred.penup()
    cred.speed(0)
    cred.setposition(-110,130)
    cred.write("\tMade By:\n Ethan Steckler and Jonah Zoller",font=fontSetup)
    cred.hideturtle()

def direction(x,y):
    wn.clearscreen()
    wn.title("Boggle")
    wn.bgcolor("#6F8FAF")
    instructions = t.Turtle()
    instructions.hideturtle()
    instructions.penup()
    instructions.goto(-500, 200)
    instructions.write("How to Play:\n Find a word by connecting letters together in a 4x4 grid.\n You can connect horizontal, diagonial, or vertical\n You can not use words you have used before and they must be real words. \n PVP: First person to 5 words wins!! \n PVC: Try and get 10 words before you get 3 strikes!", align="left", font=("Arial", 20, "bold"))
    img = t.Turtle()
    img.penup()
    img.setpos(-50,-100)
    img.shape("board.gif")

    pvps = t.Turtle()
    pvps.shape("square")
    pvps.penup()
    pvps.goto(175,-425)
    pvps.color("black")
    pvps.write("PVP",font=fontSetup)
    pvps.color("white")
    pvps.goto(125,-400)

    pvcs = t.Turtle()
    pvcs.shape("square")
    pvcs.penup()
    pvcs.goto(-175,-425)
    pvcs.color("black")
    pvcs.write("PVC",font=fontSetup)
    pvcs.color("white")
    pvcs.goto(-200,-400)

    pvps.onclick(pvp)
    pvcs.onclick(pvc)
    wn.listen()



def board():
    global player2points
    global player1points
    wn.clearscreen()
    wn.bgcolor("#6F8FAF")

    player1points = 0
    player2points = 0  

    board = t.Turtle()
    board.penup()
    board.speed(0)
    board.setposition(300,300)
    board.setheading(180)
    board.pendown()
    board.fillcolor("white")
    board.begin_fill()

    for i in range(4):
        board.forward(600)
        board.left(90)
    board.end_fill()
    board.setpos(300,175)
    board.fillcolor("white")
    board.begin_fill()
    for i in range(2):
        board.forward(600)
        board.left(90)
        board.forward(500)
        board.left(90)
    board.end_fill()
    for i in range(4):
        board.forward(150)
        board.left(90)
        board.forward(500)
        board.right(180)
        board.forward(500)
        board.setheading(180)
    board.setheading(270)
    for i in range(4):
        board.forward(125)
        board.left(90)
        board.forward(600)
        board.right(180)
        board.forward(600)
        board.setheading(270)
    y = 100
    x= -230
    row = []
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x1y1.shape(letters[rand])
    x1y1.penup()
    x1y1.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x2y1.shape(letters[rand])
    x2y1.penup()
    x2y1.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x3y1.shape(letters[rand])
    x3y1.penup()
    x3y1.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x4y1.shape(letters[rand])
    x4y1.penup()
    x4y1.setpos(x,y)
    x += 150
    bo.append(row) 
    row = []
    x = -230
    y -= 125
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x1y2.shape(letters[rand])
    x1y2.penup()
    x1y2.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x2y2.shape(letters[rand])
    x2y2.penup()
    x2y2.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x3y2.shape(letters[rand])
    x3y2.penup()
    x3y2.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x4y2.shape(letters[rand])
    x4y2.penup()
    x4y2.setpos(x,y)
    x += 150
    bo.append(row) 
    row = []
    x = -230
    y -= 125
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x1y3.shape(letters[rand])
    x1y3.penup()
    x1y3.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x2y3.shape(letters[rand])
    x2y3.penup()
    x2y3.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x3y3.shape(letters[rand])
    x3y3.penup()
    x3y3.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x4y3.shape(letters[rand])
    x4y3.penup()
    x4y3.setpos(x,y)
    x += 150
    bo.append(row) 
    row = []
    x = -230
    y -= 125
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x1y4.shape(letters[rand])
    x1y4.penup()
    x1y4.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x2y4.shape(letters[rand])
    x2y4.penup()
    x2y4.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x3y4.shape(letters[rand])
    x3y4.penup()
    x3y4.setpos(x,y)
    x += 150
    rand = random.randint(0,25)
    letter = alphabet[rand]
    row.append(letter)
    x4y4.shape(letters[rand])
    x4y4.penup()
    x4y4.setpos(x,y)
    x += 150
    bo.append(row) 
    row = []

    global points
    global reset
    scorer.penup()
    scorer.goto(-200,175)
    scorer.color("black")
    
    scorer.hideturtle()

    writer = t.Turtle()
    writer.penup()
    writer.goto(-50,250)
    writer.color("black")
    writer.hideturtle()

    submit.shape("submitbutton.gif")
    submit.penup()
    submit.goto(-400,0)

    reset.penup()
    reset.shape("resetbutton.gif")
    reset.goto(400,0)

tile = 0

word = ""
BeenClicked1 = False
BeenClicked2 = False
BeenClicked3 = False
BeenClicked4 = False
BeenClicked5 = False
BeenClicked6 = False
BeenClicked7 = False
BeenClicked8 = False
BeenClicked9 = False
BeenClicked10 = False
BeenClicked11 = False
BeenClicked12 = False
BeenClicked13 = False
BeenClicked14 = False
BeenClicked15 = False
BeenClicked16 = False

def checkIfWord(x,y):
    global points
    global word
    global BeenClicked1
    global BeenClicked2
    global BeenClicked3
    global BeenClicked4
    global BeenClicked5
    global BeenClicked6
    global BeenClicked7
    global BeenClicked8
    global BeenClicked9
    global BeenClicked10
    global BeenClicked11
    global BeenClicked12
    global BeenClicked13
    global BeenClicked14
    global BeenClicked15
    global BeenClicked16
    global scorer
    global turn
    global player1points
    global player2points
    global tile
    global usedWords

    input_word = word.lower()
    if input_word == "":
        pass
        # word = t.textinput("Boggle", "Enter a word:")
    if input_word not in usedWords:
        if is_valid_word(input_word):
            valid_word = t.Turtle()
            invalid_word = t.Turtle()
            valid_word.hideturtle()
            valid_word.penup()
            valid_word.goto(0,220)
            valid_word.write(f"{input_word.upper()} is a valid word!", align="center", font=("Arial", 16, "normal"))

            if turn == 1:
                player1points += 1
                scorer.clear()
                scorer.write(f"Player1: {player1points}  TURN! Player2: {player2points}",font=fontSetup)
                turn = 2
            elif turn == 2:
                player2points += 1
                scorer.clear()
                scorer.write(f"TURN! Player1: {player1points}  Player2: {player2points}",font=fontSetup)
                turn = 1 

            # wait for a new word to be entered before clearing the message
            usedWords.append(word)
            word = ""

        else:
            invalid_word = t.Turtle()
            valid_word = t.Turtle()
            invalid_word.hideturtle()
            invalid_word.penup()
            invalid_word.goto(0,220)
            invalid_word.write(f"{input_word.upper()} is not a valid word.", align="center", font=("Arial", 16, "normal"))
            # wait for a new word to be entered before clearing the message
            word = ""
            if turn == 1:
                turn = 2
            elif turn == 2:
                turn = 1 
        writer.clear()
        writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
        tile = 0
        invalid_word.clear()
        valid_word.clear()
    elif input_word in usedWords:
        writer.clear()
        writer.write(f"Repeated word",font=fontSetup)
    
    
    
    
        
    # replace the text in the input box with an empty string
    word = ""
    BeenClicked1 = False
    BeenClicked2 = False
    BeenClicked3 = False
    BeenClicked4 = False
    BeenClicked5 = False
    BeenClicked6 = False
    BeenClicked7 = False
    BeenClicked8 = False
    BeenClicked9 = False
    BeenClicked10 = False
    BeenClicked11 = False
    BeenClicked12 = False
    BeenClicked13 = False
    BeenClicked14 = False
    BeenClicked15 = False
    BeenClicked16 = False
    
def checkIfWordpvc(x,y):
    global points
    global strikes
    global word
    global BeenClicked1
    global BeenClicked2
    global BeenClicked3
    global BeenClicked4
    global BeenClicked5
    global BeenClicked6
    global BeenClicked7
    global BeenClicked8
    global BeenClicked9
    global BeenClicked10
    global BeenClicked11
    global BeenClicked12
    global BeenClicked13
    global BeenClicked14
    global BeenClicked15
    global BeenClicked16
    global scorer
    global turn
    global player1points
    global player2points
    global tile
    global usedWords

    input_word = word.lower()
    if input_word == "":
        pass
    if input_word not in usedWords:
        if is_valid_word(input_word):
            valid_word = t.Turtle()
            invalid_word = t.Turtle()
            valid_word.hideturtle()
            valid_word.penup()
            valid_word.goto(0,220)
            valid_word.write(f"{input_word.upper()} is a valid word!", align="center", font=("Arial", 16, "normal"))

            player1points += 1
            scorer.clear()
            scorer.write(f"Player1: {player1points}  Strikes = {strikes}",font=fontSetup)
            usedWords.append(word)
            word = ""
        
        else:
            invalid_word = t.Turtle()
            valid_word = t.Turtle()
            invalid_word.hideturtle()
            invalid_word.penup()
            invalid_word.goto(0,220)
            invalid_word.write(f"{input_word.upper()} is not a valid word.", align="center", font=("Arial", 16, "normal"))
            strikes += 1
            scorer.clear()
            scorer.write(f"Player1: {player1points}  Strikes = {strikes}",font=fontSetup)
            word = ""
        writer.clear()
        writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
        tile = 0
        invalid_word.clear()
        valid_word.clear()
    elif input_word in usedWords:
        writer.clear()
        writer.write(f"Repeated word",font=fontSetup)
    
    
    
    
        
    # replace the text in the input box with an empty string
    word = ""
    BeenClicked1 = False
    BeenClicked2 = False
    BeenClicked3 = False
    BeenClicked4 = False
    BeenClicked5 = False
    BeenClicked6 = False
    BeenClicked7 = False
    BeenClicked8 = False
    BeenClicked9 = False
    BeenClicked10 = False
    BeenClicked11 = False
    BeenClicked12 = False
    BeenClicked13 = False
    BeenClicked14 = False
    BeenClicked15 = False
    BeenClicked16 = False

def clicked1(x,y):
    global BeenClicked1
    global word
    global tile
    if tile == 0 or tile == 1 or tile == 2 or tile == 5 or tile == 6:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked1 == False:
            word += bo[0][0]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked1 = True
        elif BeenClicked1 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 1

def clicked2(x,y):
    global BeenClicked2
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 1 or tile == 2 or tile == 3 or tile == 5 or tile == 6 or tile == 7:
        writer.clear()
        if BeenClicked2 == False:
            word += bo[0][1]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked2 = True
        elif BeenClicked2 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 2

def clicked3(x,y):
    global BeenClicked3
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 2 or tile == 3 or tile == 4 or tile == 6 or tile == 7 or tile == 8:
        writer.clear()
        if BeenClicked3 == False:
            word += bo[0][2]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked3 = True
        elif BeenClicked3 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 3

def clicked4(x,y):
    global BeenClicked4
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 3 or tile == 4 or tile == 7 or tile == 8:
        writer.clear()
        if BeenClicked4 == False:
            word += bo[0][3]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked4 = True
        elif BeenClicked4 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 4

def clicked5(x,y):
    global BeenClicked5
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 1 or tile == 2 or tile == 5 or tile == 6 or tile == 9 or tile == 10:
        writer.clear()
        if BeenClicked5 == False:
            word += bo[1][0]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked5 = True
        elif BeenClicked5 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 5

def clicked6(x,y):
    global BeenClicked6
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 1 or tile == 2 or tile == 3 or tile == 5 or tile == 6 or tile == 7 or tile == 9 or tile == 10 or tile == 11:
        writer.clear()
        if BeenClicked6 == False:
            word += bo[1][1]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked6 = True
        elif BeenClicked6 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 6  
   
def clicked7(x,y):
    global BeenClicked7
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 2 or tile == 3 or tile == 4 or tile == 6 or tile == 7 or tile == 8 or tile == 10 or tile == 11 or tile == 12:
        writer.clear()
        if BeenClicked7 == False:
            word += bo[1][2]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked7 = True
        elif BeenClicked7 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 7  

def clicked8(x,y):
    global BeenClicked8
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 3 or tile == 4 or tile == 7 or tile == 8 or tile == 11 or tile == 12:
        writer.clear()
        if BeenClicked8 == False:
            word += bo[1][3]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked8 = True
        elif BeenClicked8 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 8

def clicked9(x,y):
    global BeenClicked9
    global word
    global tile
    writer.penup()
    writer.goto(-50,250)
    if tile == 0 or tile == 5 or tile == 6 or tile == 9 or tile == 10 or tile == 13 or tile == 14:
        writer.clear()
        if BeenClicked9 == False:
            word += bo[2][0]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked9 = True
        elif BeenClicked9 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 9

def clicked10(x,y):
    global BeenClicked10
    global word
    global tile
    if tile == 0 or tile == 5 or tile == 6 or tile == 7 or tile == 9 or tile == 10 or tile == 11 or tile == 13 or tile == 14 or tile == 15:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked10 == False:
            word += bo[2][1]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked10 = True
        elif BeenClicked10 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 10

def clicked11(x,y):
    global BeenClicked11
    global word
    global tile
    if tile == 0 or tile == 6 or tile == 7 or tile == 8 or tile == 10 or tile == 11 or tile == 12 or tile == 14 or tile == 15 or tile == 16:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked11 == False:
            word += bo[2][2]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked11 = True
        elif BeenClicked11 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 11

def clicked12(x,y):
    global BeenClicked12
    global word
    global tile
    if tile == 0  or tile == 7 or tile == 8 or tile == 11 or tile == 12 or tile == 15 or tile == 16:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked12 == False:
            word += bo[2][3]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked12 = True
        elif BeenClicked12 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 12    

def clicked13(x,y):
    global BeenClicked13
    global word
    global tile
    if tile == 0 or tile == 9 or tile == 10 or tile == 13 or tile == 14:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked13 == False:
            word += bo[3][0]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked13 = True
        elif BeenClicked13 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 13   

def clicked14(x,y):
    global BeenClicked14
    global word
    global tile
    if tile == 0 or tile == 9 or tile == 10 or tile == 11 or tile == 13 or tile == 14 or tile == 15:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked1 == False:
            word += bo[3][1]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked14 = True
        elif BeenClicked14 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 14

def clicked15(x,y):
    global BeenClicked15
    global word
    global tile
    if tile == 0 or tile == 10 or tile == 11 or tile == 12 or tile == 14 or tile == 15 or tile == 16:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked15 == False:
            word += bo[3][2]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked15 = True
        elif BeenClicked15 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 15

def clicked16(x,y):
    global BeenClicked16
    global word
    global tile
    if tile == 0 or tile == 11 or tile == 12 or tile == 15 or tile == 16:
        writer.clear()
        writer.penup()
        writer.goto(-50,250)
        if BeenClicked16 == False:
            word += bo[3][3]
            writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
            print(word)
            BeenClicked16 = True
        elif BeenClicked16 == True:
            writer.write(f"Word: {word}  Already Used that letter", align="center", font=("Arial", 24, "normal"))
        tile = 16

def resets(x,y):
    global word
    global BeenClicked1
    global BeenClicked2
    global BeenClicked3
    global BeenClicked4
    global BeenClicked5
    global BeenClicked6
    global BeenClicked7
    global BeenClicked8
    global BeenClicked9
    global BeenClicked10
    global BeenClicked11
    global BeenClicked12
    global BeenClicked13
    global BeenClicked14
    global BeenClicked15
    global BeenClicked16
    global tile
    word = ""
    writer.clear()
    writer.write(f"Word: {word}", align="center", font=("Arial", 24, "normal"))
    BeenClicked1 = False
    BeenClicked2 = False
    BeenClicked3 = False
    BeenClicked4 = False
    BeenClicked5 = False
    BeenClicked6 = False
    BeenClicked7 = False
    BeenClicked8 = False
    BeenClicked9 = False
    BeenClicked10 = False
    BeenClicked11 = False
    BeenClicked12 = False
    BeenClicked13 = False
    BeenClicked14 = False
    BeenClicked15 = False
    BeenClicked16 = False
    tile = 0

def pvp(x,y): 
    global submit 
    global x1y1
    global x1y2
    global x1y3
    global x1y4
    global x2y1
    global x2y2
    global x2y3
    global x2y4
    global x3y1
    global x3y2
    global x3y3
    global x3y4
    global x4y1
    global x4y2
    global x4y3
    global x4y4
    global scorer

    board()
    
    scorer.write(f"TURN! Player 1: {player1points}  Player 2: {player2points}",font=fontSetup)
    print(bo)

    while player1points != 5 and player2points != 5:
        x1y1.onclick(clicked1)
        x2y1.onclick(clicked2)
        x3y1.onclick(clicked3)
        x4y1.onclick(clicked4)
        x1y2.onclick(clicked5)
        x2y2.onclick(clicked6)
        x3y2.onclick(clicked7)
        x4y2.onclick(clicked8)
        x1y3.onclick(clicked9)
        x2y3.onclick(clicked10)
        x3y3.onclick(clicked11)
        x4y3.onclick(clicked12)
        x1y4.onclick(clicked13)
        x2y4.onclick(clicked14)
        x3y4.onclick(clicked15)
        x4y4.onclick(clicked16)


        submit.onclick(checkIfWord)
        reset.onclick(resets)
        wn.listen()
    
    if player1points == 5:
        scorer.clear()
        scorer.write(f"Player1 WINS!",font=fontSetup)
    elif player2points == 5:
        scorer.clear()
        scorer.write(f"Player2 WINS!",font=fontSetup)
    
def pvc(x,y):
    global submit 
    global x1y1
    global x1y2
    global x1y3
    global x1y4
    global x2y1
    global x2y2
    global x2y3
    global x2y4
    global x3y1
    global x3y2
    global x3y3
    global x3y4
    global x4y1
    global x4y2
    global x4y3
    global x4y4
    global scorer

    board()  
    scorer.write(f"Goal: Find 10 words without failing 3 times!",font=fontSetup)
    print(bo)

    while player1points != 10 and strikes != 3:
        x1y1.onclick(clicked1)
        x2y1.onclick(clicked2)
        x3y1.onclick(clicked3)
        x4y1.onclick(clicked4)
        x1y2.onclick(clicked5)
        x2y2.onclick(clicked6)
        x3y2.onclick(clicked7)
        x4y2.onclick(clicked8)
        x1y3.onclick(clicked9)
        x2y3.onclick(clicked10)
        x3y3.onclick(clicked11)
        x4y3.onclick(clicked12)
        x1y4.onclick(clicked13)
        x2y4.onclick(clicked14)
        x3y4.onclick(clicked15)
        x4y4.onclick(clicked16)


        submit.onclick(checkIfWordpvc)
        reset.onclick(resets)
        wn.listen()
    
    if player1points == 10:
        scorer.clear()
        scorer.write(f"YOU WINS!",font=fontSetup)
    elif strikes == 3:
        scorer.clear()
        scorer.write(f"YOU LOSE!",font=fontSetup)


credits.onclick(credit)
tutorial.onclick(direction)
pvps.onclick(pvp)
pvcs.onclick(pvc)
wn.listen()
wn.mainloop()
import random
import string
p1Score=0
p2Score=0
p1Turn=0
x1=[random.choice(string.ascii_lowercase) for i in range(4)]
x2=[random.choice(string.ascii_lowercase) for i in range(4)]
x3=[random.choice(string.ascii_lowercase) for i in range(4)]
x4=[random.choice(string.ascii_lowercase) for i in range(4)]
def refresh():
    x1=[random.choice(string.ascii_lowercase) for i in range(4)]
    x2=[random.choice(string.ascii_lowercase) for i in range(4)]
    x3=[random.choice(string.ascii_lowercase) for i in range(4)]
    x4=[random.choice(string.ascii_lowercase) for i in range(4)]
    y1=rowBuilder(x1)
    y2=rowBuilder(x2)
    y3=rowBuilder(x3)
    y4=rowBuilder(x4)
def rowBuilder(x):
        y=""
        for i in range(len(x)):
            if i!=len(x)-1:
                y+=x[i]+" "
            else:
                y+=x[i]
        return y 
y1=rowBuilder(x1)
y2=rowBuilder(x2)
y3=rowBuilder(x3)
y4=rowBuilder(x4)
table=f"""
		 ⬜⬜⬜⬜⬜⬜
		 ⬜ {y1}⬜
		 ⬜ {y2}⬜
		 ⬜ {y3}⬜
		 ⬜ {y4}⬜
		 ⬜⬜⬜⬜⬜⬜
		"""
if (p1Turn % 2) == 0:
    p1Turn==True
else:
    p1Turn==False
#  This code is contributed by divyesh072019.
def dfs(board, s, i, j, n, m, idx):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if s[idx] != board[i][j]:
        return False
    if idx == len(s) - 1:
        return True
    temp = board[i][j]
    board[i][j] = '*'
    a = dfs(board, s, i, j+1, n, m, idx+1)
    b = dfs(board, s, i, j-1, n, m, idx+1)
    c = dfs(board, s, i+1, j, n, m, idx+1)
    d = dfs(board, s, i-1, j, n, m, idx+1)
    e = dfs(board, s, i+1, j+1, n, m, idx+1)
    f = dfs(board, s, i-1, j+1, n, m, idx+1)
    g = dfs(board, s, i+1, j-1, n, m, idx+1)
    h = dfs(board, s, i-1, j-1, n, m, idx+1)
    board[i][j] = temp
    return a or b or c or e or f or g or h or d
 
def wordBoggle(board, dictionary):
    n = len(board)
    m = len(board[0])
    store = set()
     
    #     Let the given dictionary be following
    for word in dictionary:
        for i in range(n):
            for j in range(m):
                if dfs(board, word, i, j, n, m, 0):
                    store.add(word)
# -------------------------------------
boggle = [[x1],
          [x2],
          [x3],
          [x4]]
dictionary = open("Dict.txt", 'r').read().splitlines()
for i in range(len(dictionary)):
    dictionary[i]=dictionary[i].lower()
def check():
    global p1Score
    global p2Score
    global p1Turn
    print(table)
    if p1Turn==True:
        print(f"Player 2 Score: {p1Score}")
    else:
        print(f"Player 1 Score: {p2Score}")
    ui=input("Enter a word on the board or q to refresh: ")
    if ui in dictionary:
        print(f"{ui} is a word on the board! +1 point.")
        if p1Turn==True:
            p1Score+=1
            dictionary.remove(ui)
        else:
            p2Score+=1
            dictionary.remove(ui)
    elif ui=="q" or ui=="Q":
            refresh()
    else:
        print(f"{ui} is not on the board! -1 point.")
        if p1Turn==True:
            p1Score-=1
        else:
            p2Score-=1
    p1Turn+=1
while p1Score<=10 or p2Score<=10:
    wordBoggle(boggle,dictionary)
    check()

import turtle
bob = turtle.Turtle()
var = turtle.Turtle()
wn = turtle.Screen()
bob.speed(50)
bob.color('white')
var.speed(50)
var.color('white')
wn.bgcolor('black')
bob.hideturtle()
var.hideturtle()
bob.goto(0,0)
gameOver = False
a = int(turtle.textinput('Place holder', 'choose a number between 3 and 9'))
arr = ['None'] * (a**2)
var.penup()
var.goto(a*50//2,a*50+50)
var.write('X turn', align='center', font=('Arial',20, 'normal'))
wn.screensize(a*500,a*500)
res = []
turn = 0
z = [[(int(i%a)*50), int(50 * (i//a)) if int(i) % a == 0 else int(i//a * 50)] for i in range(a**2)]
def f(arr):
    e = [arr[i*a:(i+1)*a] for i in range(a)][::-1]
    b = [arr[i::a] for i in range(a)]
    c = [e[-i][::-1][i] for i in range(a)]
    d = [e[i][i] for i in range(a)]
    return e+b+[c]+[d]
def board():
    for i in range(a+1):
        bob.goto(50*a,50*i)
        bob.penup()
        bob.goto(0, 50*(i+1))
        bob.pendown()
    bob.penup()
    bob.goto(0, 0)
    bob.pendown()
    for i in range(a+1):
        bob.goto(50*i,50*a)
        bob.penup()
        bob.goto(50*(i+1),0)
        bob.pendown()
board()
def cords(x, y):
    global gameOver
    if not gameOver:
        global z
        bob.up()
        global turn
        if x < 0 or y < 0 or x > a * 50 or  y > a * 50:
            pass
        elif [x//50 * 50,y//50 * 50] not in res:
            turn += 1
            bob.goto(x//50 * 50,y//50 * 50)
            if turn % 2 == 0: 
                var.clear()
                var.goto(a*50//2,a*50+50)
                var.write('X turn', align='center', font=('Arial',20, 'normal'))    
                z[z.index([x//50 * 50,y//50 * 50])] =  'O'
                bob.color('red')
                bob.penup()
                bob.goto(x//50 * 50 + 25,y//50 * 50 + 5)
                bob.pendown()
                bob.circle(40/2)
                bob.up()
            else:
                var.clear()                
                var.goto(a*50//2,a*50+50)
                var.write('O turn', align='center', font=('Arial',20, 'normal'))
                z[z.index([x//50 * 50,y//50 * 50])] = 'X'
                bob.color('blue')
                bob.penup()
                bob.goto(x//50 * 50 + 10 ,y//50 * 50 + 10)
                bob.pendown()
                bob.goto(x//50 * 50 + 50 - 10,y//50 * 50 + 50- 10)
                bob.penup()
                bob.goto(x//50 * 50 + 10,y//50 * 50 + 50 - 10)
                bob.pendown()
                bob.goto(x//50 * 50 + 50 - 10 ,y//50 * 50 + 10)
        if [x//50 * 50,y//50 * 50] not in res: res.append([x//50 * 50,y//50 * 50])
        arr = ['None' if type(z[i]) == list else z[i] for i,v in enumerate(z)]
        win = ([i for i in f(arr) if len(set(i)) == 1 and 'None' not in i])
        if win:   
            gameOver = True
            bob.penup()
            bob.goto(a*50//2,-50)
            bob.write(f'{win[0][0]} is the winner!', align='center', font=('Arial',20, 'normal'))
        elif turn == a**2:
            bob.color('green')
            bob.penup()
            bob.goto(a*50//2,-50)
            bob.write(f'Tie!', align='center', font=('Arial',20, 'normal'))
turtle.onscreenclick(cords)
wn.mainloop()

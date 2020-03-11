import turtle

wn = turtle.Screen()
wn.title("Crazy Tennis")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#punteggio

score_a =0
score_b= 0

#Giocatore a
giocatore_a = turtle.Turtle()
giocatore_a.speed(0)
giocatore_a.shape("square")
giocatore_a.color("white")
giocatore_a.shapesize(stretch_wid = 5 ,stretch_len = 1)

giocatore_a.penup()
giocatore_a.goto(-350,0)
#giocatore b
giocatore_b = turtle.Turtle()
giocatore_b.speed(0)
giocatore_b.shape("square")
giocatore_b.color("white")
giocatore_b.shapesize(stretch_wid = 5 ,stretch_len = 1)

giocatore_b.penup()
giocatore_b.goto(350,0)
# palla 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

ball.penup()
ball.goto(0,0)

#movimento della palla 
ball.dx = 2
ball.dy= 2

#pen
pen = turtle.Turtle()
pen .speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0", align="center",font=("Couruer",24, "normal"))




#funzioni
def giocatore_a_up():
    y = giocatore_a.ycor()
    y+=20
    giocatore_a.sety(y)

def giocatore_a_down():
    y = giocatore_a.ycor()
    y-=20
    giocatore_a.sety(y)

def giocatore_b_up():
    y = giocatore_b.ycor()
    y+=20
    giocatore_b.sety(y)

def giocatore_b_down():
    y = giocatore_b.ycor()
    y-=20
    giocatore_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(giocatore_a_up,"w")

wn.onkeypress(giocatore_a_down,"s")

wn.onkeypress(giocatore_b_up,"Up")

wn.onkeypress(giocatore_b_down,"Down")
#Main game loop

while True:
    wn.update()

    # Palla che si muove
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )

    # bordo
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b), align="center",font=("Couruer",24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b), align="center",font=("Couruer",24, "normal"))



    # collisione con la racchetta
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < giocatore_b.ycor() + 40 and ball.ycor() > giocatore_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < giocatore_a.ycor()+ 40 and ball.ycor() > giocatore_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
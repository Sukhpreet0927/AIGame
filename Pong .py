import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=900, height=600)
window.tracer(0)

#Paddle 1 for player 1
Paddle_1 = turtle.Turtle()
Paddle_1.speed(0)
Paddle_1.shape("square")
Paddle_1.shapesize(stretch_wid=5, stretch_len=1)#resize shape of paddle
Paddle_1.color("blue")
Paddle_1.penup()
Paddle_1.goto (-400, 0)

#Paddle 2 for player 2
Paddle_2 = turtle.Turtle()
Paddle_2.speed(0)
Paddle_2.shape("square")
Paddle_2.shapesize(stretch_wid=5, stretch_len=1)#resize shape of paddle
Paddle_2.color("red")
Paddle_2.penup()
Paddle_2.goto(400, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Ball Movement (movement by x amount of pixel)
ball.dx = 1
ball.dy = 1

#Movements
def Paddle_1_up():
    y = Paddle_1.ycor()
    y += 30
    Paddle_1.sety(y)
def Paddle_1_down():
    y = Paddle_1.ycor()
    y -= 30
    Paddle_1.sety(y)
def Paddle_2_up():
    y = Paddle_2.ycor()
    y += 30
    Paddle_2.sety(y)
def Paddle_2_down():
    y = Paddle_2.ycor()
    y -= 30
    Paddle_2.sety(y)

#Title
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 235)
pen.write("Pong", align= "center", font=("Comic Sans MS", 38, "bold"))

#Keybinds
window.listen()
window.onkeypress(Paddle_1_up, "w")
window.onkeypress(Paddle_1_down, "s")
window.onkeypress(Paddle_1_up, "W")
window.onkeypress(Paddle_1_down, "S")
window.onkeypress(Paddle_2_up, "Up")
window.onkeypress(Paddle_2_down, "Down")

#Scoring system
pen_1 = turtle.Turtle()
pen_1.color("blue")
pen_1.speed(0)
pen_1.penup()
pen_1.hideturtle()
pen_1.goto(-250, 245)
pen_1.write("Player One: 0", align= "center", font=("Comic Sans MS", 22, "bold"))
pen_2 = turtle.Turtle()
pen_2.color("red")
pen_2.speed(0)
pen_2.penup()
pen_2.hideturtle()
pen_2.goto(250, 245)
pen_2.write("Player Two: 0", align= "center", font=("Comic Sans MS", 22, "bold"))
score_1 = 0
score_2 = 0



#All collisions
while True:
    window.update()
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Boundries (reverses direction when ball hits causing dy to be in a negative direction)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -286:
        ball.sety(-286)
        ball.dy *= -1
    #Paddle boundries
    if Paddle_1.ycor() > 260:
        Paddle_1.sety(260)
    if Paddle_1.ycor() < -260:
        Paddle_1.sety(-260)
    if Paddle_2.ycor() > 260:
        Paddle_2.sety(260)
    if Paddle_2.ycor() < -260:
        Paddle_2.sety(-260)
    #Scoring update for player one
    if ball.xcor() > 450:
        ball.sety(0)
        ball.setx(0)
        ball.dx *= -1
        pen_1.clear()
        score_1 += 1
        pen_1.write("Player One: {}".format(score_1), align="center", font=("Comic Sans MS", 22, "bold"))
    #Winner
    if score_1 == 10:
        ball.hideturtle()
        Paddle_1.hideturtle()
        Paddle_2.hideturtle()
        pen_1.hideturtle()
        pen_2.hideturtle()
        pen_3 = turtle.Turtle()
        pen_3.color("yellow")
        pen_3.speed(0)
        pen_3.penup()
        pen_3.hideturtle()
        pen_3.goto(0, 0)
        pen_3.write("Player One WINS", align="center", font=("Comic Sans MS", 22, "bold"))
    #Scoring update player two
    if ball.xcor() < -450:
        ball.sety(0)
        ball.setx(0)
        ball.dx *= -1
        pen_2.clear()
        score_2 += 1
        pen_2.write("Player Two: {}".format(score_2), align="center", font=("Comic Sans MS", 22, "bold"))
    #Winner
    if score_2 == 10:
        ball.hideturtle()
        Paddle_1.hideturtle()
        Paddle_2.hideturtle()
        pen_1.hideturtle()
        pen_2.hideturtle()
        pen_4 = turtle.Turtle()
        pen_4.color("yellow")
        pen_4.speed(0)
        pen_4.penup()
        pen_4.hideturtle()
        pen_4.goto(0, 0)
        pen_4.write("Player Two WINS", align="center", font=("Comic Sans MS", 22, "bold"))
    #Bounce (of paddle a)
    if (ball.xcor() < -378 and ball.xcor() < -378) and ball.ycor() < Paddle_1.ycor() + 50 and ball.ycor() > Paddle_1.ycor() - 50:
        ball.setx(-378)
        ball.dx *= -1
    #Bounce (of paddle b)
    if (ball.xcor() > 378 and ball.xcor() > 378) and ball.ycor() < Paddle_2.ycor() + 50 and ball.ycor() > Paddle_2.ycor() - 50:
        ball.setx(378)
        ball.dx *= -1


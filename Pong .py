import turtle
import time

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=900, height=600)
window.tracer(0)

#Paddle 1 for player 1
class Paddle(turtle.Turtle):
    def __init__(self, speed, shapesize, color, x, y):
        super().__init__(shape='square')
        self.speed(speed)  # Set the turtle speed based on the passed value
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.y = y
        self.x = x

    def get_speed(self):
        return self.speed

    def get_y(self):
        return self.y  
    
    def set_y(self, y):
        self.y = y

    def hide(self):
        self.hideturtle()

 
P1 = Paddle(0, shapesize=(5, 1), color="blue", x=400, y=0)
P2 = Paddle(0, shapesize=(5, 1), color="red", x=-400, y=0)

#print(P1.get_speed())


#Paddle_1 = turtle.Turtle()
# Paddle_1.speed(0)
# Paddle_1.shape("square")
# Paddle_1.shapesize(stretch_wid=5, stretch_len=1)#resize shape of paddle
# Paddle_1.color("blue")
# self.penup()
# Paddle_1.goto (-400, 0)

#Paddle 2 for player 2
# Paddle_2 = turtle.Turtle()
# Paddle_2.speed(0)
# Paddle_2.shape("square")
# Paddle_2.shapesize(stretch_wid=5, stretch_len=1)#resize shape of paddle
# Paddle_2.color("red")
# Paddle_2.penup()
# Paddle_2.goto(400, 0)
#Ball
class Ball(turtle.Turtle):
    def __init__(self, speed, color, x, y, dx, dy):
        super().__init__(shape='circle')
        self.speed(speed)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.y = y
        self.x = x
        self.dx = dx
        self.dy = dy


        # self.turtle = turtle.Turtle()
        # self.turtle.speed(speed)  # Set the turtle speed
        # self.turtle.shape(shape)
        # self.turtle.color(color)
        # self.turtle.penup()
        # self.turtle.goto(x, y)
        # self.y = y
        # self.x = x
        # self.dx = dx
        # self.dy = dy

    def get_speed(self):
        return self.speed

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x  
    
    def get_dx(self):
        return self.dx
    
    def get_dy(self):
        return self.dy
    
    def set_dy(self, dy):
        self.dy = dy

    def set_dx(self, dx):
        self.dx = dx
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def hide(self):
        self.hideturtle()



ball = Ball(speed = 0, color = "white", x = 0,y = 0, dx = 1, dy =1)



# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape("circle")
# ball.color("white")
# ball.penup()
# ball.goto(0, 0)

# #Ball Movement (movement by x amount of pixel)
# ball.dx = 1
# ball.dy = 1

#Movements

def Paddle_1_up():
    P1.set_y(P1.get_y() + 30) 
    # y = Paddle_1.ycor()
    # y += 30
    # Paddle_1.sety(y)
def Paddle_1_down():
    P1.set_y(P1.get_y() - 30) 
    # y = Paddle_1.ycor()
    # y -= 30
    # Paddle_1.sety(y)
def Paddle_2_up():
    P2.set_y(P2.get_y() + 30) 
    # y = Paddle_2.ycor()
    # y += 30
    # Paddle_2.sety(y)
def Paddle_2_down():
    P2.set_y(P2.get_y() - 30) 
    # y = Paddle_2.ycor()
    # y -= 30
    # Paddle_2.sety(y)

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

#ball = turtle.Turtle()
# ball.speed(0)
# ball.shape("circle")
# ball.color("white")
# ball.penup()
# ball.goto(0, 0)

# #Ball Movement (movement by x amount of pixel)
#ball.dx = 1
#ball.dy = 1
while True:
    window.update()
    #Ball Movement
    ball.set_x(ball.get_x() + ball.get_dx())
    ball.set_y(ball.get_y() + ball.get_dy())
    #ball.set_y(ball.ycor() + ball.dy)
    #Boundries (reverses direction when ball hits causing dy to be in a negative direction)
    if ball.get_y() > 290:
        ball.set_y(290)
        ball.set_dy(ball.get_dy() * -1)
        #ball.dy *= -1
    if ball.get_y() < -286:
        ball.set_y(-286)
        ball.set_dy(ball.get_dy() * -1)
        
        # ball.sety(-286)
        # ball.dy *= -1
    #Paddle boundries
    if P1.get_y() > 260:
        P1.set_y(260)
    if P1.get_y() < -260:
        P1.set_y(-260)
    if P2.get_y() > 260:
        P2.set_y(260)
    if P2.get_y() < -260:
        P2.set_y(-260)
    #Scoring update for player one
    if ball.get_x() > 450:
        ball.set_y(0)
        ball.set_x(0)
        ball.set_dx(ball.get_dx() * -1)
        pen_1.clear()
        score_1 += 1
        pen_1.write("Player One: {}".format(score_1), align="center", font=("Comic Sans MS", 22, "bold"))
    #Winner
    if score_1 == 10:
        ball.hide()
        P1.hide()
        P2.hide()
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
    if ball.get_x() < -450:
        ball.set_y(0)
        ball.set_x(0)
        ball.set_dx(ball.get_dx() * -1)
        pen_2.clear()
        score_2 += 1
        pen_2.write("Player Two: {}".format(score_2), align="center", font=("Comic Sans MS", 22, "bold"))
    #Winner
    if score_2 == 10:
        ball.hide()
        P1.hide()
        P2.hide()
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
    if (ball.get_x() < -378 and ball.get_x() < -378) and ball.get_y() < P1.get_y() + 50 and ball.get_y() > P1.get_y() - 50:
        ball.set_x(-378)
        ball.set_dx(ball.get_dx() * -1)
        #ball.dx *= -1
    #Bounce (of paddle b)
    if (ball.get_x() > 378 and ball.get_x() > 378) and ball.get_y() < P2.get_y() + 50 and ball.get_y() > P2.get_y() - 50:
        ball.set_x(378)
        ball.set_dx(ball.get_dx() * -1)
        #ball.dx *= -1



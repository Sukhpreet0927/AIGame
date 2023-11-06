import turtle
import os
import pygame
import neat
import time
import pickle

#Boundary
Boundary = turtle.Turtle()
Boundary.penup()
Boundary.pensize(20)
Boundary.speed(0)
Boundary.goto(-450, -300)
Boundary.color("white")
Boundary.pendown()
Boundary.forward(900)
Boundary.left(90)
Boundary.forward(600)
Boundary.left(90)
Boundary.forward(900)
Boundary.left(90)
Boundary.forward(600)

class GameInformation:
       def __init__(self, left_hits, right_hits, left_score, right_score):
              self.left_hits = left_hits
              self.right_hits = right_hits
              self.left_score = left_score
              self.right_score = right_score


#Game itself loop

class Paddle(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        if y < 240:  # Adjust the limit as needed
            y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        if y > -240:  # Adjust the limit as needed
            y -= 20
        self.sety(y)

    def get_y(self):
        return self.ycor()

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

# Create the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create the players
paddle_a = Paddle(-350, 0, "blue")
paddle_b = Paddle(350, 0, "red")

# Create the ball
ball = Ball()

# Create the pen for displaying the scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 235)
pen.write("Pong", align= "center", font=("Comic Sans MS", 38, "bold"))

# Set initial state for ball movement
game_started = False

#Score
score_a = 0
score_b = 0

# Function to start the game
def start_game():
	global game_started
	game_started = True
	# global game_started
	# game_started = True

# Keyboard bindings
wn.listen()
wn.onkeypress(start_game, "space")
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

# Left and right
if ball.xcor() > 350:
	score_a += 1
	pen.clear()
	pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	ball.goto(0, 0)
	ball.dx *= -1
# Left and right
if ball.xcor() > 350:
	score_a += 1
	pen.clear()
	pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	ball.goto(0, 0)
	ball.dx *= -1

elif ball.xcor() < -350:
	score_b += 1
	pen.clear()
	pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	ball.goto(0, 0)
	ball.dx *= -1
elif ball.xcor() < -350:
	score_b += 1
	pen.clear()
	pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
	ball.goto(0, 0)
	ball.dx *= -1

# #Ball Movement (movement by x amount of pixel)
# ball.dx = 1
# ball.dy = 1
def Gameloop(left_hits, right_hits, score_a, score_b):
    #Score
    while True:
        wn.update()

        
        # Move the ball
        if game_started:
            # Move the ball
            # ball.setx(ball.xcor() + ball.dx)
            # ball.sety(ball.ycor() + ball.dy)
            ball.move()

        # if(wn.onkeypress("space")) :
        #     ball.setx(ball.xcor() + ball.dx)
        #     ball.sety(ball.ycor() + ball.dy)

        # Border checking
            # Top and bottom
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
        
            elif ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1

            # Left and right
            if ball.xcor() > 350:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1

            elif ball.xcor() < -350:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1

            # Paddle and ball collisions
            if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                left_hits += 1 
                ball.dx *= -1

                #os.system("afplay bounce.wav&")
            
            elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
                right_hits += 1
                ball.dx *= -1
                #os.system("afplay bounce.wav&")

            


            if score_a == 5:
                ball.hideturtle()
                paddle_a.hideturtle()
                paddle_b.hideturtle()
                wn.listen()
                paddle_a.setposition(1000, 1000)
                paddle_b.setposition(1100 , 1000)
                win_1 = turtle.Turtle()
                win_1.speed(0)
                win_1.color("white")
                win_1.penup()
                win_1.hideturtle()
                win_1.goto(0, 0)
                win_1.write("Player 1 is the winner", align = "center", font = ("Impact", 28, "normal"))
                GG_1 = turtle.Turtle()
                GG_1.speed(0)
                GG_1.color("yellow")
                GG_1.penup()
                GG_1.hideturtle()
                GG_1.goto(0, -175)
                GG_1.write("Good Game", align = "center", font = ("Impact", 36, "bold"))
                game_info = GameInformation(left_hits, right_hits, score_a, score_b)
                return game_info
            

            if score_b == 5:
                ball.hideturtle()
                paddle_a.hideturtle()
                paddle_b.hideturtle()
                wn.listen()
                paddle_a.setposition(1000, 1000)
                paddle_b.setposition(1100 , 1000)
                win_2 = turtle.Turtle()
                win_2.speed(0)
                win_2.color("white")
                win_2.penup()
                win_2.hideturtle()
                win_2.goto(0, 0)
                win_2.write("Player 2 is the winner", align = "center", font = ("Impact", 28, "normal"))
                GG_2 = turtle.Turtle()
                GG_2.speed(0)
                GG_2.color("green")
                GG_2.penup()
                GG_2.hideturtle()
                GG_2.goto(0, -175)
                GG_2.write("Good Game", align = "center", font = ("Impact", 36, "bold"))
                game_info = GameInformation(left_hits, right_hits, score_a, score_b)
                return game_info





if __name__ == '__main__':
        left_hits = 0
        right_hits = 0 
        score_a = 0 
        score_b = 0
        
        game_info = Gameloop(left_hits, right_hits, score_a, score_b)


        # Print the game information
        print("Game Information:")
        print(f"Left Hits: {game_info.left_hits}")
        print(f"Right Hits: {game_info.right_hits}")
        print(f"Left Score: {game_info.left_score}")
        print(f"Right Score: {game_info.right_score}")

        
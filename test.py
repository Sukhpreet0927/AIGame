#testing
import turtle
from Pong import Paddle, Ball, pen, GameInformation
import neat
import os
import pickle


class AiPongGame:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)


        self.left_paddle = Paddle(-350, 0, "blue")
        self.right_paddle = Paddle(350, 0, "red")
        self.ball = Ball()

        self.setup_keybindings() #Call the setup_keybindings method

    # Add this method to your AiPongGame class
    def setup_keybindings(self):    
        self.wn.listen()
        self.wn.onkeypress(self.left_paddle.move_up, "w")
        self.wn.onkeypress(self.left_paddle.move_down, "s")
        self.wn.onkeypress(self.right_paddle.move_up, "Up")
        self.wn.onkeypress(self.right_paddle.move_down, "Down")






    def test_ai(self, genome, config):
            net1 = neat.nn.FeedForwardNetwork.create(genome, config)
            score_a = 0
            score_b = 0
            left_hits = 0
            right_hits = 0
            run = True
            while run:
                self.wn.update()
                self.ball.move()


                # Border checking
                # Top and bottom
                if self.ball.ycor() > 290:
                    self.ball.sety(290)
                    self.ball.dy *= -1
            
                elif self.ball.ycor() < -290:
                    self.ball.sety(-290)
                    self.ball.dy *= -1

                # Left and right
                if self.ball.xcor() > 350:
                    score_a += 1
                    pen.clear()
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1

                elif self.ball.xcor() < -350:
                    score_b += 1
                    pen.clear()
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1

                # Paddle and ball collisions
                if self.ball.xcor() < -340 and self.ball.ycor() < self.left_paddle.ycor() + 50 and self.ball.ycor() > self.left_paddle.ycor() - 50:
                    left_hits += 1 
                    self.ball.dx *= -1

                    #os.system("afplay bounce.wav&")
                
                elif self.ball.xcor() > 340 and self.ball.ycor() < self.right_paddle.ycor() + 50 and self.ball.ycor() > self.right_paddle.ycor() - 50:
                    right_hits += 1
                    self.ball.dx *= -1


                input2 = [self.right_paddle.get_y(), self.ball.ycor(), abs(self.right_paddle.xcor() - self.ball.xcor())]
                output2 = net1.activate(input2)
                decision2 = output2.index(max(output2))

                


                if decision2 == 0:
                    pass
                elif decision2 == 1:
                    self.right_paddle.move_up()
                else:
                    self.right_paddle.move_down()

                game_info = GameInformation(left_hits, right_hits, score_a, score_b)

            
                
                

    def train_ai(self, genome1, genome2, config):
            net1 = neat.nn.FeedForwardNetwork.create(genome1, config) #neural networks
            net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        
            run = True
            #Score
            score_a = 0
            score_b = 0
            left_hits = 0
            right_hits = 0
            



            while run:
                self.wn.update()
                self.ball.move()
                



                # Border checking
            # Top and bottom
                if self.ball.ycor() > 290:
                    self.ball.sety(290)
                    self.ball.dy *= -1
            
                elif self.ball.ycor() < -290:
                    self.ball.sety(-290)
                    self.ball.dy *= -1

                # Left and right
                if self.ball.xcor() > 350:
                    score_a += 1
                    pen.clear()
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1

                elif self.ball.xcor() < -350:
                    score_b += 1
                    pen.clear()
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1

                # Paddle and ball collisions
                if self.ball.xcor() < -340 and self.ball.ycor() < self.left_paddle.ycor() + 50 and self.ball.ycor() > self.left_paddle.ycor() - 50:
                    left_hits += 1 
                    self.ball.dx *= -1

                    #os.system("afplay bounce.wav&")
                
                elif self.ball.xcor() > 340 and self.ball.ycor() < self.right_paddle.ycor() + 50 and self.ball.ycor() > self.right_paddle.ycor() - 50:
                    right_hits += 1
                    self.ball.dx *= -1



                # Prepare input values for both neural networks
                input1 = [self.left_paddle.get_y(), self.ball.ycor(), abs(self.left_paddle.xcor() - self.ball.xcor())]
                input2 = [self.right_paddle.get_y(), self.ball.ycor(), abs(self.right_paddle.xcor() - self.ball.xcor())]

    
                # Activate the neural networks
                output1 = net1.activate(input1)
                decision1 = output1.index(max(output1))

                if decision1 == 0:
                    pass
                elif decision1 == 1:
                    self.left_paddle.move_up()
                else:
                    self.left_paddle.move_down()
                
                
                output2 = net2.activate(input2)
                decision2 = output2.index(max(output2))

                


                if decision2 == 0:
                    pass
                elif decision2 == 1:
                    self.right_paddle.move_up()
                else:
                    self.right_paddle.move_down()

        
    
                print(output1, output2)

                game_info = GameInformation(left_hits, right_hits, score_a, score_b)

                #print(game_info.left_hits)
                #print(game_info.right_hits)

                #game_info = Gameloop(0,0,0,0)

                if game_info.left_score >= 1 or game_info.right_score >= 1 or game_info.left_score > 50:
                     self.calculate_fitness(genome1, genome2, game_info)
                     self.left_paddle.hideturtle()
                     self.right_paddle.hideturtle()
                     self.ball.hideturtle()

                     break
            
    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits
         


def eval_genomes(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
         if i == len(genomes) - 1:
              break
         genome1.fitness = 0
         for genome_id2, genome2 in genomes[i+1:]:
              genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
              game = AiPongGame()
              game.train_ai(genome1, genome2, config)
              



def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-0')
    p = neat.Population(config)
    print("fasfsadfads")
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1)) #restart training cause it could take a while
    
    winner = p.run(eval_genomes, 1)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)

def test_ai(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    game = AiPongGame()
    game.test_ai(winner, config)


    
if __name__ == "__main__":
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, "config.txt")

        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)
        
        run_neat(config)
        #test_ai(config)
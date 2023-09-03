#testing
import turtle
import pygame
from Pong import *
import neat
import os
import pickle

class AiPongGame:
    def __init__(self):
        self.left_paddle = Paddle(-350, 0, "blue")
        self.right_paddle = Paddle(350, 0, "red")
        self.ball = Ball()

    def test_ai(self, genome, config):
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            run = True
            clock = pygame.time.Clock()
            while run:
                wn.update()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break
                game_info = Gameloop(0, 0, 0, 0) 
                print(game_info.left_score, game_info.right_score)
                

    def train_ai(self, genome1, genome2, config):
            wn = turtle.Screen()
            net1 = neat.nn.FeedForwardNetwork.create(genome1, config) #neural networks
            net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        
            run = True
            while run:
                wn.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                
                # Prepare input values for both neural networks
                input1 = [self.left_paddle.get_y(), self.ball.ycor(), abs(self.left_paddle.xcor() - ball.xcor())]
                input2 = [self.right_paddle.get_y(), self.ball.ycor(), abs(self.right_paddle.xcor() - ball.xcor())]
    
                # Activate the neural networks
                output1 = net1.activate(input1)
                decision1 = output1.index(max(output1))

                if decision1 == 0:
                    pass
                elif decision1 == 1:
                    self.left_paddle.hideturtle()
                    self.left_paddle.move_up(up = True)
                else:
                    self.left_paddle.hideturtle()
                    self.left_paddle.move_down(down = True)
                
                
                output2 = net2.activate(input2)
                decision2 = output2.index(max(output2))

                


                if decision2 == 0:
                    pass
                elif decision2 == 1:
                    self.right_paddle.move_up(up = True)
                else:
                    self.right_paddle.move_down(down = True)

        
    
                print(output1, output2)

                game_info = Gameloop(0,0,0,0)

                if game_info.left_score >= 5 or game_info.right_score >= 5 or game_info.left_hits > 5:
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
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1)) #restart training cause it could take a while
    winner = p.run(eval_genomes, 50)


    
if __name__ == "__main__":
        pygame.init()
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, "config.txt")

        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)
        # run_neat(config)
        run_neat(config)



#Rock Paper Scissor Generator

# For this project, you and your partner(s) will work to create a program that has a "player" and a "computer" adversary.
# The computer should randomly choose its decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). 
# The player should then have a chance to input their decision. 

  #  if rock > scissor = rock (wins)
  #  if rock < paper = paper (wins)
  #  if scissor < rock = rock (wins)
  # if scissor > paper = scissor (wins)
  # if paper > rock = paper (wins)
  # if paper < scissor = scissor (wins)
  # {"Rock", "Paper", "Scissors"}
  # input("What is your decision?")
  # Computer vs. Player (us)
  # randomgenerator

import random

def rock_paper_scissor():
    user = input("What is your choice? 'rock' for rock, 'paper' for paper, 'scissors' for scissors\n")
    computer = random.choice(['rock','paper','scissors'])

    if user == computer:
        return 'It is a tie! You: {} Computer: {}.'.format(user,computer)

    # r > s, s > p, p > r
    if wins(user, computer):
        return "You won! You: {} Computer: {}".format(user, computer)
    return "You lost! You: {} Computer: {}".format(user,computer)
    
def wins(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        return False

def game():
     while 


    
print(rock_paper_scissor())

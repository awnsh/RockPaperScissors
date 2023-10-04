'''
This project uses a series of if loops, lists, the input function, and a library, which includes different possibilites of what can occur if the bot or user picks something. It is a simple Rock Paper Scissors game. This version requires the user to pick an amount they want to play until. Click the "Run" button or Ctrl + Enter to play.
Made by Awnsh

     @@@@@@                               @@@@@@  
    @@@@@@@@@                          @@@@@@@@@  
    @@@@@@@@@@@         @@@@#        @@@@@@@@@@@  
    @@@@@@@@@@@@@     @@@@@@@@      @@@@@@ @@@@@  
    @@@@@@  @@@@@@   @@@@@@@@@@@  @@@@@@@  @@@@@  
    @@@@@@   @@@@@@@@@@@@@ @@@@@@@@@@@@    @@@@@ 
    @@@@@@     @@@@@@@@@    @@@@@@/@@@     @@@@@  
    @@@@@@      @@@@@@@       @@@@@@       @@@@@  
     @@@@@@  @@@@@@@@          *@@@@@@@@@@@@@@@@  
      @@@@@@@@@@@@@              @@@@@@@@@@@@@@   
         @@@@@@                      @@@@@@@      
'''

#allows to run loop again
def game():
  
  import random
  
  score = 0
  botscore = 0
  
  i = "y"
  
  #asks the use what score they would like to play until
  playtill = input("What do you want to play until (1-20): ")
  print()
  print("===================================")

  #makes user put a number 
  try:
    #makes user to put a value higher than 1
    if int(playtill) <= 0:
      print("Please input a value higher than 0")
      exit()

  except:
    if not str(playtill.isdigit()):
      pass
    #makes user to put a value lower than 20
    if int(playtill) > 20:
      print("Please input a value less than 20")
      exit()

    else:
      print("Please put a number 1-20")
      exit()

  
  while True:
      
    #prints user's and bot's score
    print("Bot: " + str(botscore) + " Score: " + str(score))
    print()
  
    #the list for the options to choose
    hand = ['rock', 'paper', 'scissors']
  
    #takes user choice
    usera = input('Rock, Paper or Scissors?: ')
    
    #makes user choice lowercase 
    user = usera.lower()
    
    #stores bot choice in choice variable
    choice = random.choice(hand)

    #makes user print Rock, Paper, or Scissors
    if user != "rock" and user != "paper" and user != "scissors":
      print()
      print("Please input Rock, Paper, or Scissors")

    
    #rock possibilites
    if user == 'rock' and choice == 'paper':
      print()
      print('The bot picked ' + choice)
      print('Paper covers rock, You lost')
      botscore = botscore + 1 
      
    if user == 'rock' and choice == 'rock':
      print()
      print('The bot picked ' + choice)
      print('Its a tie!')
    
    if user == 'rock' and choice == 'scissors':
      print()
      print('The bot picked ' + choice)
      print('Rock breaks scissors, You Won!')
      score = score + 1
  
      
    #paper possibilites
    if user == 'paper' and choice == 'scissors':
      print()
      print('The bot picked ' + choice)
      print('Scissors cuts paper, You Lost')
      botscore = botscore + 1 
    
    if user == 'paper' and choice == 'rock':
      print()
      print('The bot picked ' + choice)
      print('Paper covers rock, You Won!')
      score = score + 1
    
    if user == 'paper' and choice == 'paper':
      print()
      print('The bot picked ' + choice)
      print('Its a tie!')
    
    
    #scissors possibilites 
    if user == 'scissors' and choice == 'rock':
      print()
      print('The bot picked ' + choice)
      print('Rock breaks scissors, You Won')
      score = score + 1 
    
    if user == 'scissors' and choice == 'paper':
      print()
      print('The bot picked ' + choice)
      print('Scissors cuts paper, You lost!')
      botscore = botscore + 1
    
    if user == 'scissors' and choice == 'scissors':
      print()
      print('The bot picked ' + choice)
      print('Its a tie!')
  
    print()
    print("===================================")
    print()

    #says user won the game when they reach the score they inputted
    if score == int(playtill):
      print("You got "+ str(playtill) + " first. You won the game!")
      break

    #says bot won the game when they reach the score it inputted
    if botscore == int(playtill):
      print("The bot got "+ str(playtill) + " first. You lost the game!")
      break
  
  #asks the user if they want to play again
  print()
  playagains = str(input("Would you like to play again? y/n: "))
  print()
  print("===================================")
  print()
  playagain = playagains.lower()
  if playagain == i:
    game()
  else:
    exit()

game()

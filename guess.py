# Variables
rand = 0 # for higher or lower
guess = 0 # for guess my number
flip = 0 # for heads or tails
ans = 10000000000 # var. for guess my number/ending a game
wins = 0 # counts amount of wins
num = 0 # answer given by player
guesses = 0 # counts amount of guesses the player has given
give = 0 # counts amount of times the player has given up


import random

# Start of game
begin = input('Would you like to play? ')

if begin == "yes":
    input('Which game should we play? (Higher or lower, Guess my number, Heads or tails). (type "Give up" to end the game) Or type "Score" to see how many times you have won and amount of guesses you had')
    
    if input == "score":
       print("Wins: " + wins)
       print("Guesses: " + guesses)
       print("Times given up: " + give)

    if input == "Guess my Number": # Guess my number code
        input('How high should I count to? ')
        ans = random.randrange(input)
        while num != ans:
           input('What do you think is the number? ')
           if input == "Give up":
               num = ans
               give + 1
           if input > ans: # If ans is to high
              print("To high :(")
           elif input < ans: # If ans is to low
              print("To low :(")
           else: # Got it correct
             print("You won! :)")
             wins + 1
             input('Do you want to play again? ')
             if input == "yes":
                num = num
             else:
                num == ans


    elif input == "Higher or lower": # Higher or lower code
       print("Lets play higher or lower")
       input('Would you like to play or I play? ("Player" for you, "Com" for the computer) ')
       if input == "Player":
          input('What range do you want me to pick from 0- ')
          rand = random.randrange(input)
          while num != num:
             input('Guess a number ')
             if input > rand:
                print("To high")
             if input < rand:
                print("To low")
             else:
                print("you got it!")
                wins + 1
             

    elif input == "Heads or tails": # Heads or tails code
        print("Lets play heads or tails")
        while num != ans:
           flip = random.randrange(1)
           input('Heads or tails? (1 = heads and 0 = tails) ')
           if input == "Give up":
              num == ans
              give + 1
           if input == flip:
              print("You got it right!")
              wins + 1
              input('Do you want to play again? ')
              if input == "yes":
                 num = num
              else:
                 num == ans
           else:
              guesses + 1
              print("Your chance of winning was 50%, try again :/")
              

# If player doesn't want to play
else:
   print("Goodbye :(")

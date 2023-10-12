# Variables
rand = 0 # for higher or lower
guess = 0 # for guess my number player
com_guess = 0 # for guess my number com
flip = 0 # for heads or tails
end = 10000000000 # end game
wins = 0 # counts amount of wins
num = 0 # answer given by player
guesses = 0 # counts amount of guesses the player has given
give = 0 # counts amount of times the player has given up
game = "waiting" # takes in input for selected game
limit = 0 # Limit of number player chooses
inp = 0 # player input for guess my number
choice = "yes" # for higher or lower

import random

# Start of game
begin = input('Would you like to play? ')

if begin == "yes":
    game = input('Which game should we play? (Higher or lower, Guess my number, Heads or tails). (type "Give up" to end the game) Or type "Score" to see how many times you have won and amount of guesses you had ')
    
    if game == "score":
       print("Wins: " + wins)
       print("Guesses: " + guesses)
       print("Times given up: " + give)

    elif game == "Guess my Number": # Guess my number code
        limit = input("How high should I count to?" )
        guess = random.randint(limit)
        while num != end:
           inp = input('What do you think is the number? ')
           if inp == "Give up":
               num = end
               give + 1
           if inp > guess: # If ans is to high
              print("To high :(")
           elif inp < guess: # If ans is to low
              print("To low :(")
           else: # Got it correct
             print("You won! :)")
             wins + 1
             begin = input('Do you want to play again? ')
             if input == "yes":
                num = num
             else:
                num = end


    elif game == "Higher or lower": # Higher or lower code
       print("Lets play higher or lower")
       choice = input('Would you like to play or I play? ("Player" for you, "Com" for the computer) ')
       if choice == "Player":
          limit = input('What range do you want me to pick from 0-')
          rand = random.randint(input)
          while num != num:
             input('Guess a number ')
             if input > rand:
                print("To high")
             if input < rand:
                print("To low")
             else:
                print("you got it!")
                wins + 1
       elif input == "Com":
          limit = input('What range are you picking from 0-')
          rand = random.randint(input)
          com_guess = rand
          while num != num:
             print("Is your number " + com_guess + "?")
             input('yes or no?')
             if input == "no": # Com guesses wrong
                input('Is it higher or lower? ')
                if input == "higher": # To high
                   com_guess = random.randint()
                elif input == "lower": # To low
                   com_guess = random.randint(com_guess)
             
             if input == "yes": # Com guesses correctly
                print("Yay!")
                input('Do you want to play again? ')
             if input == "yes": # End game?
                num = num
             else:
                num == end
             if input == "Give up": # End game
                num = end   
             
             

    elif game == "Heads or tails": # Heads or tails code
        print("Lets play heads or tails")
        while num != end:
           flip = random.randrange(1) # Decides heads or tails
           input('Heads or tails? (1 = heads and 0 = tails) ')
           if input == "Give up":
              num = end
              give + 1
           if input == flip:
              print("You got it right!")
              wins + 1
              input('Do you want to play again? ')
              if input == "yes":
                 num = num
              else:
                 num = end
           else: # If player gets it wrong
              guesses + 1
              print("Your chance of winning was 50%, try again :/")
              

# If player doesn't want to play
else:
   print("Goodbye :(")

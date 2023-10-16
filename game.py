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
HOrT = "waiting" # takes input for heads or tails
endLoop = "waiting" # var. for ending the game
minV = 0 # min value
maxV = 0 # max value

import random

# Start of code
begin = input('Would you like to play? ')

while begin == "yes":
    game = input('Which game should we play? (Higher or lower, Guess my number, Heads or tails).' 
               '(type "Give up" to end the game) (Type "end" to end the loop)' 
               '(Type "Score" to see how many times you have won and amount of guesses you had) ')
    
    if game == "Score":
       print("Wins: " + str(wins))
       print("Guesses: " + str(guesses))
       print("Times given up: " + str(give))

    elif game == "Guess my number": # Guess my number code
        limit = input("How high should I count to? " )
        guess = random.randint(0, int(limit))
        while num != end:
           inp = input('What do you think is the number? ')
           inp = int(inp)
           if inp == "Give up":
               num = end
               give + 1
           if inp > guess: # If ans is to high
              print("To high :(")
              guesses =+ 1
           elif inp < guess: # If ans is to low
              print("To low :(")
              guesses =+ 1
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
          rand = random.randint(0, int(limit))
          while num != num:
             num = input('Guess a number ')
             num = int(num)
             if num > rand:
                print("To high")
             if num < rand:
                print("To low")
             else:
                print("you got it!")
                wins + 1
       elif choice == "Com":
          maxV = input('What range are you picking from 0-')
          
          while num != num:
             rand = random.randint(int(minV), int(maxV))
             com_guess = rand
             print("Is your number " + com_guess + "?")
             input('yes or no?')
             if choice == "no": # Com guesses wrong
                choice = input('Is it higher or lower? ')
                if choice == "higher": # To high
                   minV = com_guess
                elif choice == "lower": # To low
                   maxV = com_guess
             if choice == "yes": # Com guesses correctly
                print("Yay!")
                endLoop = input('Do you want to play again? ')
             if endLoop == "yes": # End game?
                num = num
             else:
                num = end
             if num == "Give up": # End game
                num = end   
             
             

    elif game == "Heads or tails": # Heads or tails code
        print("Lets play heads or tails")
        while num != end:
           flip = random.randrange(0, 1) # Decides heads or tails
           HOrT = input('Heads or tails? (1 = heads and 0 = tails) ')
           if HOrT == "Give up":
              num = end
              give + 1
           if HOrT == flip:
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
    if game == "end":
       break
#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #start of the game
colors = ['red','orange','yellow','green','blue','violet','purple'] #tells you which variables it accepts
play_again = ''                          #Descibes the play again comment at the end
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #descibes whats going on in the indented stuff after this
    match_color = random.choice(colors) #it sets the syetem up to make a random color the correct answer for each new round.
    count = 0                       #sets the count for the ending guess count
    color = ''                     #lets the system know that the color is going to be typed in by the user
    while (color != match_color):   #this sets the value for color equal to the color the system randomly produced
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()       #this is the part that allows for spacing and capitalization errors
        count += 1                     #everytime theres a new round the count goes up by one
        if (color == match_color):               #if the color is the one that that system chose as the random right color....
            print('Correct!')                   #...the system will display correct
        else:                                   #if its a different color....
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))   #....it will display a wrong answer along with the number of guesses for the round
    print('\nYou guessed it in {0} tries!'.format(count))  #tells the system to display the you guessed it in X ammount of tries message
    if (count < best_count):     #this ties in to past rounds, if the number of guesses was less than the lasyt round there will be a message for it
        print('This was your best guess so far!')     #this is the message that displays if there is a best guess
        best_count = count          #this is what tells the system what the meaning of best guess is
    play_again = input("\nWould you like to play again? ").lower().strip()          #after the round there will be a message for playing again
print('Thanks for playing!')     #if you answer no or n the game will display a thank you message 
import random #added imported file 
print ("Welcome to Guess the Number!")
print ("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)

isGuessRight = False #if the guessed number is wrong, enter the loop

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ") #user will guess a number bewteen 1-10
    if int(guess) == number:
        print(f" You guessed {guess}. That is correct! You win!") #if the number is guessed correctly, this will be the response
        
    else:
        print(f" You guessed {guess}. Sorry, that isn't it. Try again.")
        #if the user guesses incorrectly, this will be the response, until the correct numner is guessed
    
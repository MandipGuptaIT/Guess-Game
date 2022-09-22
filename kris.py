
import random
randNumber = random.randint(1, 999)
#print(randNumber)      # Not print cause we dont have to show the guessed no.
user = None 
guesses = 0

while(user != randNumber):
    user = int(input("Enter your guess: "))
    guesses += 1
    if(user== randNumber):
        print("You guesses it right")
    else:
        if(user>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")


#It's save your High Score in .txt

with open("highscore.txt", "r")as f:
    highscore = int(f.read())


if(guesses<highscore):
    print("You have just the broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))

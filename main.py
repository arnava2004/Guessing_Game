import random
words=["Giraffe", "Elephant","Code","Python"]
secret_word=words[random.randint(0,len(words)-1)]

guess_count= 0
guesses=4
while guesses>0:
    guess=input("What is your guess? ")
    if guess==secret_word:
        print("Correct! It took you " + str(guess_count+1) + " try")
        guesses=0
    else:
        print("Incorrect! You have " + str(guesses-guess_count-1) + " tries left")
        guesses -=1
print("The secret word was " + secret_word + "!")

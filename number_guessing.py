import random

print("Welcome to the Number Guessing Game!")
print("i've thinking of a number between 1 and 100")

answer = random.randint(1,100)
print(f"The correct answer is {answer}")


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
    def set_difficulty():
        level = input("choose a dificulty. type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    def check_answer(guess, answer, turns):
        if guess > answer:
            print("too high")
            return turns - 1
        elif guess < answer:
            print("too low")
            return turns - 1
        else:
            print(f"you got it! the answer is {answer}")


    turns = set_difficulty()
    guess = 0
    
    while guess != answer:  
        print(f"You have {turns} attempts remaining to guess the number.")
    
        guess = int(input("make a guess: "))

        turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of the guesses,  you loose.")
    elif guess != answer:
        print("Guess again!")

        return

game()

import random
import turtle
import requests

def draw_head():
    turtle.penup()
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.circle(20)
    turtle.speed(1)  # Set turtle speed to slow for better visibility

def draw_body():
    turtle.penup()
    turtle.goto(0, -20)  # Starting point of the body
    turtle.pendown()
    turtle.goto(0, -100)
    turtle.speed(1)  # Set turtle speed to slow for better visibility

def draw_leftarm():
    turtle.penup()
    turtle.goto(0, -30)  # Starting point of the arms
    turtle.pendown()
    turtle.goto(-30, -50)  # Left arm
    turtle.speed(1)  # Set turtle speed to slow for better visibility

def draw_rightarm():
    turtle.penup()
    turtle.goto(0, -30)  # Reset to the starting point
    turtle.pendown()
    turtle.goto(30, -50)  # Right arm
    turtle.speed(1)  # Set turtle speed to slow for better visibility

def draw_leftleg():
    turtle.penup()
    turtle.goto(0, -100)  # Starting point of the legs
    turtle.pendown()
    turtle.goto(-30, -150)  # Left leg
    turtle.speed(1)  # Set turtle speed to slow for better visibility

def draw_rightleg():
    turtle.penup()
    turtle.goto(0, -100)  # Reset to the starting point
    turtle.pendown()
    turtle.goto(30, -150)  # Right leg
    turtle.speed(1)  # Set turtle speed to slow for better visibility


def get_word_from_file():
    try:
        with open('movielist.txt', 'r') as file:
            words = file.readlines()
        if words:
            return random.choice([word.strip().lower().replace(' ',',') for word in words])  # Convert to lowercase
        else:
            return 'cryptosystem'  # Default fallback word if file is empty
    except FileNotFoundError:
        print("Words file not found. Defaulting to 'cryptosystem'.")
        return 'cryptosystem'  # Default fallback word if file is not found

def display_word(word, guessed_letters):
    vowels = "aeiouAEIOU"
    characters = "!@#$%^&*()_+-=}{][:;<>,.?/\|"
    return ''.join([char if char in vowels or char in characters or char in guessed_letters else '_' for char in word])

def hangman():
    word = get_word_from_file()
    guessed_letters = set()
    vowels = "aeiouAEIOU"
    attempts = 6
    guess_word = display_word(word, guessed_letters)

    print("Let's play Hangman!!!")
    print(f"Your word: {guess_word}")

    while attempts > 0 and '_' in guess_word:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed the letter.")
            continue
        if guess in vowels:
            print("You are entering a vowel, please enter a consonant. Thank you.")
            continue
        guessed_letters.add(guess)

        if guess in word:
            print("Correct!!")
        else:
            attempts -= 1
            if attempts == 5:
                draw_head()
            elif attempts == 4:
                draw_body()
            elif attempts == 3:
                draw_rightarm()
            elif attempts == 2:
                draw_leftarm()
            elif attempts == 1:
                draw_rightleg()
            elif attempts == 0:
                draw_leftleg()
            print("attempts left:{0}".format(attempts))
        guess_word = display_word(word, guessed_letters)
        print("Current word: {0}".format(guess_word))

    if '_' not in guess_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"You ran out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()
    turtle.done()

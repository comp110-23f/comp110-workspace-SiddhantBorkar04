"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730652641"

#  Box color initialization
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#  Variable Declarations and initializations
secret_word: str = "python"
input_guess: str = ""
secret_word_index: int = 0
result_emoji: str = ""
char_exsist: bool = False
alt_index: int = 0

#  Gets initial user input
input_guess = input("What is your 6-letter guess? ")

#  Runs if guess is correct
if (secret_word == input_guess):
    while (secret_word_index < len(secret_word)):
        result_emoji += GREEN_BOX
        secret_word_index += 1
    print(result_emoji)
    print("Woo! You got it!")

#  Runs if guess is not correct to determine whites and yellows
while (secret_word != input_guess):
    if (len(input_guess) == len(secret_word)):
        #  Nested Loop
        while (secret_word_index < len(secret_word)): 
            if (secret_word[secret_word_index] == input_guess[secret_word_index]):
                result_emoji += GREEN_BOX
            else:
                while ((char_exsist is not True) & (alt_index < len(secret_word))):
                    if (secret_word[alt_index] == input_guess[secret_word_index]):
                        char_exsist = True
                    alt_index += 1
                alt_index = 0
                if (char_exsist is True):
                    result_emoji += YELLOW_BOX
                    char_exsist = False
                else:
                    result_emoji += WHITE_BOX
            secret_word_index += 1
        print(result_emoji)
        print("Not quite. Play again soon!")
        break
    else:
        input_guess = input("That was not 6 letters! Try again: ")
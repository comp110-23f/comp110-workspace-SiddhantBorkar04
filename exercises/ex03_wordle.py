"""EX03 - Worlde."""


__author__ = "730652641"

#  Box color initialization
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Iterates through word variable to see if char variable is present."""
    assert len(char) == 1
    i: int = 0
    while (i < len(word)):
        if (word[i] == char):
            return True
        else:
            i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Compares parameter 1 and 2 characters, then returns the comparison as an emoji string."""
    assert len(guess_word) == len(secret_word)
    final_emoji: str = ""
    
    # While loop with counter to compare and add boxes
    counter: int = 0
    while (counter < len(secret_word)):
        # Checks if secret_word and guess_word are the same, and if so, adds green box
        if (guess_word[counter] == secret_word[counter]):
            final_emoji += GREEN_BOX
        # Checks if character is the same, but placement is wrong, and if so, adds yellow box
        elif (contains_char(secret_word, guess_word[counter])):
            final_emoji += YELLOW_BOX
        # If the previous conditions aren't met, a white box is added, because the character is not present
        else:
            final_emoji += WHITE_BOX
        counter += 1
        
    return final_emoji


def input_guess(expected_length: int) -> str:
    """Ensures that input word is of appropriate length."""
    # gathers initial user input word
    input_word: str = input("Enter a " + str(expected_length) + " character word: ")
    
    # Checks if length is correct, and if not, repeatedly asks for new input
    while (len(input_word) != expected_length):
        input_word_again: str = input("That wasn't " + str(expected_length) + " chars! Try again: ")
        input_word = input_word_again
    
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Variable Declarations
    secret_word: str = "codes"
    turn_num: int = 1
    win: bool = False
    current_guess = ""
    
    # Turn regulation and functions
    while ((turn_num <= 6) & (win is False)):
        print(f"=== Turn {turn_num}/6 ===")
        # Prompts the user for a guess and store it
        current_guess = input_guess(len(secret_word))
        
        # emojify the guess and print
        print(emojified(current_guess, secret_word))

        # if the guess is correct, wins game. If not, next turn. 
        if (current_guess == secret_word):
            win = True
        else:
            turn_num += 1

    # Win or loss, final output
    if (win is True):
        print(f"You won in {turn_num}/6 turns!")
    elif (win is False):
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
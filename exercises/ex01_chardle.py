"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730652641"

# Part 1 - Prompting for Inputs
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")  # Part 4
    exit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")  # Part 4
    exit()

print("Searching for " + character + " in " + word)

# Part 2 - Checking Indices for Matches
counter: int = 0  # Part 3 - Counting Matching Indices
if word[0] == character:
    print(character + " found at index " + str(0))
    counter += 1
if word[1] == character:
    print(character + " found at index " + str(1))
    counter += 1
if word[2] == character:
    print(character + " found at index " + str(2))
    counter += 1
if word[3] == character:
    print(character + " found at index " + str(3))
    counter += 1
if word[4] == character:
    print(character + " found at index " + str(4))
    counter += 1

if counter > 1:
    print(str(counter) + " instances of " + character + " found in " + word)
if counter == 1:
    print(str(counter) + " instance of " + character + " found in " + word)
if counter == 0:
    print("No instances of " + character + " found in " + word)
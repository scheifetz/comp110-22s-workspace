"""Exersise 01, chardle."""
__author__ = "730481771"

guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

search_chr: str = input("Enter a single character: ")
if len(search_chr) != 1:
    print("Error: Character must be a single character.")
    exit()


print("Searching for " + search_chr + " in " + guess_word)
count: int = 0

if guess_word[0] == search_chr:
    print(search_chr + " found at index 0")
    count = count + 1

if guess_word[1] == search_chr:
    print(search_chr + " found at index 1")
    count = count + 1

if guess_word[2] == search_chr:
    print(search_chr + " found at index 2")
    count = count + 1

if guess_word[3] == search_chr:
    print(search_chr + " found at index 3")
    count = count + 1

if guess_word[4] == search_chr:
    print(search_chr + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + search_chr + " found in " + guess_word)

if count == 1:
    print("1 instance of " + search_chr + " found in " + guess_word)

if count >= 2:
    print(str(count) + " instances of " + search_chr + " found in " + guess_word)
import os
import pprint

books_path = "./books"

for filename in os.listdir(books_path):
    filepath = os.path.join(books_path, filename)
    with open(filepath, "r") as file:
        print(f"\n---------- {filename} Report ----------\n")
        text = file.read()
        words = text.split()
        num_words = len(words)
        print(f"number of words: {num_words}\n")
        chars = list(text)
        letters = {}
        for char in chars:
            if char.isalpha():
                letters[char.lower()] = letters.get(char.lower(), 0) + 1
        print("letter frequency:\n")
        print(" " + pprint.PrettyPrinter().pformat(letters)[1:-1] + "\n")

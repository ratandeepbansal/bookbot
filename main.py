from sys import argv, exit
from stats import number_of_words, number_of_characters, sorted_characters

def read_file():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    with open(argv[1], 'r') as f:
        file_content = f.read()
        return file_content
# Example usage
text = read_file()
#print(f"{number_of_words(text)} total words")
#number_of_characters(text)
sorted_characters(text)
# The code reads a text file and counts the number of words in it.
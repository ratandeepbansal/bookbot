def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    text = text.lower()
    return_dict = {}
    print(len(text))
    for char in text:
        if char.isalpha():
            if char in return_dict:
                return_dict[char] += 1
            else:
                return_dict[char] = 1
    print(return_dict)

def sorted_characters(text):
    text = text.lower()
    return_dict = {}
    for char in text:
        if char.isalpha():
            if char in return_dict:
                return_dict[char] += 1
            else:
                return_dict[char] = 1
    sorted_dict = dict(sorted(return_dict.items(), key=lambda item: item[1], reverse=True))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")
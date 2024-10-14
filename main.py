def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    count_number_of_letters(file_contents)


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    print(f"{count} words are found in the document")

def count_number_of_letters(text):
    lowercase = text.lower()
    letter_occurrence = {}
    for letter in lowercase:
        if letter in letter_occurrence:
            letter_occurrence[letter] += 1
        else:
            letter_occurrence[letter] = 1
    print(letter_occurrence)


main()
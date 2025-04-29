#counts the number of words
def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

# counts the occurrence of symbols
def count_number_of_letters(text):
    lowercase = text.lower()
    letter_occurrence = {}
    for letter in lowercase:
        if letter in letter_occurrence:
            letter_occurrence[letter] += 1
        else:
            letter_occurrence[letter] = 1
    return letter_occurrence

# organizes a sorted list with dictionaries as its elements which contain the frequency of letters encoded in a format
# which allows for easy access
def created_culled_sorted_list(text):
    culled_list = []
    dictionary = {}
    lowercase = text.lower()
    split_text = lowercase.split()
    for word in split_text:
        for letter in word:
            if letter.isalpha():
                if letter in dictionary:
                    dictionary[letter] += 1
                else:
                    dictionary[letter] = 1
    for letter in dictionary:
        dummy_dict = {"character": letter, "frequency": dictionary[letter]}
        culled_list.append(dummy_dict)
    culled_list.sort(reverse=True, key=lambda x: x["frequency"])
    return culled_list

# prints a report on how often each letter appears within the text, sorted by its frequency
def print_frequency_report(text):
    culled_list = created_culled_sorted_list(text)
    count = count_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for letter in culled_list:
        print(f"{letter['character']}: {letter['frequency']}")
    print("--- End report---")
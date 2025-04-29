from stats import count_words
from stats import count_number_of_letters
from stats import created_culled_sorted_list
from stats import print_frequency_report

def main():
    print(f"{count_words(file_contents)} words found in the document")
    print_frequency_report(file_contents)
    
# imports the book
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

main()
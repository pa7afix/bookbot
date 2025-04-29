import sys

from stats import count_words
from stats import count_number_of_letters
from stats import created_culled_sorted_list
from stats import print_frequency_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # imports the bookcd
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the document")
    print_frequency_report(file_contents)

if __name__ == "__main__":
    main()
    
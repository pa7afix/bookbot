def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#        print(file_contents)
    count_words(file_contents)

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    print(count)

main()
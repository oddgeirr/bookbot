from stats import wordcount, letter_count, dictionary_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = wordcount(text)
    num_letters = letter_count(text)
    sorted_dictionary = dictionary_sort(num_letters)
    print(f"""============ BOOKBOT ============
            Analyzing book found at {path}...
            ----------- Word Count ----------""")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
 
main()
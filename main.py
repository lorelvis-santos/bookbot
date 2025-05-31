from stats import count_words, count_characters, print_report
import sys

def get_file_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        print("There was an error during runtime")
        sys.exit(1)

def main():
    path = sys.argv[1]
    text = get_file_text(path)

    words_count = count_words(text)
    characters_dictionary = count_characters(text)

    print_report(path, words_count, characters_dictionary)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

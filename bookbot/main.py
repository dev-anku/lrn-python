import sys

from stats import get_num_words, get_char_dict, CharacterCount, sorted_list


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    output = sorted_list(char_dict)
    print_report(path, num_words, output)


def print_report(path: str, num_words: int, output: list[CharacterCount]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in output:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()

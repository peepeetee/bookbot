import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = count_words(book)
    character_counts = count_characters(book)
    sorted_list = sort_characters(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_dict in sorted_list:
        if character_dict["name"].isalpha():
            print(f"{character_dict["name"]}: {character_dict["num"]}")
    print("============= END ===============")

    return 0

main()
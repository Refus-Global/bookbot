from stats import count_words, count_characters, sort_character_counts
import sys



def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    
    
    word_count = len(book_text.split())
    print(f"Word Count: {word_count}")
    
    
    char_count = count_characters(book_text)
    print("Character Count:")
    
    
    for char, count in char_count.items():
        print(f"'{char}': {count}")
    
   
    count_words(book_text)
    
    sorted_char_counts = sort_character_counts(char_count)
    
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()


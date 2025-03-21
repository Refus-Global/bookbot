def count_words(text):
   
    words = text.split()
    num_words = len(words)
    
    
    print(f"{num_words} words found in the document")

def count_characters(text: str) -> dict:
    
    text = text.lower()

    
    char_count = {}

    
    for char in text:
        if char in char_count:
            
            char_count[char] += 1
        else:
            
            char_count[char] = 1

    return char_count

def sort_character_counts(char_count_dict):
    
    sorted_counts = sorted(
        [{"char": char, "count": count} for char, count in char_count_dict.items() if char.isalpha()],
        key=lambda x: x["count"],
        reverse=True
    )
    return sorted_counts
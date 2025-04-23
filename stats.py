def count_words(book_string):
    words = book_string.split()
    return len(words)

def count_characters(book_string):
    #change all characters to lower case
    book_string = book_string.lower()

    words = book_string.split()
    character_counts = {}
    for word in words:
        for character in word:
            if character in character_counts:
                character_counts[character] += 1
            else: character_counts[character] = 1
    return character_counts

def sort_on(dict):
    return dict["num"]

def sort_characters(character_counts):
    list = []
    for item in character_counts:
        list.append({"name": item, "num": character_counts[item]})

    list.sort(reverse = True, key = sort_on)
    return(list)

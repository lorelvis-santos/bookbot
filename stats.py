def count_words(str):
    return len(str.split())

def count_characters(str):
    characters = {}

    for character in str.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] = characters[character] + 1
    
    return characters

def sort_dict(dict):
    return dict["number"]

def sort_characters(characters_count):
    characters_list = []

    for current in characters_count:
        if current.isalpha():
            characters_list.append({
                "char": current,
                "number": characters_count[current]
            })

    characters_list.sort(key=sort_dict, reverse=True)

    return characters_list

def print_report(path, words_count, characters_dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    
    for character in characters_dictionary:
        print(f"{character["char"]}: {character["number"]}")
    
    print("============= END ===============")

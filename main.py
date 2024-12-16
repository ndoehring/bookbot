def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    chars_sorted_list = get_character_count_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for i in chars_sorted_list:
        print(f"The {i["char"]} character was found {i["num"]} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

#gets number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)

#Creates dictionary of the number of times each character is present
def get_character_count(text):
    character_count = {}
    l_text = text.lower()
    for i in l_text:
        if i.isalpha() == True:
            if i not in character_count.keys():
                character_count[i] = 1
            elif i in character_count.keys():
                previous_count = character_count[i]
                character_count[i] = (previous_count + 1)              
    return(character_count)

#Puts the character dictionary into a list of dictionaries and sorts by most seen first
def get_character_count_list(character_count):
    list_character_count = []
    for k, v in character_count.items():
        list_character_count.append({"char": k, "num": v})
    list_character_count.sort(reverse=True, key=sort_on)
    return list_character_count

#defines key to sort by
def sort_on(e):
    return e["num"]







main()
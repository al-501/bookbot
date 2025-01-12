def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    characters = character_count(text)
    report = list_sort(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(text):
    characters = {}
    for i in text:
        lowered = i.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(d):
    return d["num"]

def list_sort(dict):
    sorted = []
    for ch in dict:
        sorted.append({"char": ch, "num": dict[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted    

main()
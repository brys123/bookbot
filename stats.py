def get_book_text(path): # get book text from file and return text
    #print(f"Attempting to open: {path}")
    with open(path) as f:
        return f.read()
    
def get_num_words(text): # uses get_book_text to get the number of words in the book
    num_words = text.split()
    return len(num_words)

def get_dict(chars): # counts each character in a dicionary using get_book_text
    words = chars.lower()
    letters = {}

    for letter in words:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    list = []
    for char, count in letters.items():
        list.append({
            "char": char,
            "num": count
        })
    return list

def sort_on(dict): #dict sorter
    return dict["num"]

def sorted_list(dict):
    # Get list from text_counter
    unsorted = dict
    # Sort it using sort_on()
    sorted_letters = sorted(unsorted, key=sort_on, reverse=True)
    return sorted_letters
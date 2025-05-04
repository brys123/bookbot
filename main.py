import sys
from stats import get_book_text, get_dict, get_num_words, sorted_list

def main():
    if len(sys.argv) < 2: #check if we are getting the book path
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] # turn the book path into a variable
        text = get_book_text(book_path) #plug in the book path and read all text
        num_words = get_num_words(text) # get number of words using getnumwords function
        dict = get_dict(text) #turn the letters into dicts
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        for item in sorted_list(dict): #turn the dictionaries into a list of dicts and print neatly
            print(f"{item['char']}: {item['num']}")
        print(f"============= END ===============")

main()
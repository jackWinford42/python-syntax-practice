word_list = ["hello", "hey", "goodbye", "yo", "yes", "electric", "China", "tree", "zoo", "parallel", "Holland"]

def print_upper_words(list_of_words, letter_set):
    """Given a list of words and a set of letters
    this function will print each word starting with one of those
    letters and capitalize every letter in that word"""
    for word in word_list:
        for letter in letter_set:
            if word[0] == letter or word[0] == letter.capitalize():
                print(word.upper())

print_upper_words(word_list, letter_set=("h","y","c"))
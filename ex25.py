def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.popp(0)
    print word

def print _last_word(words):
    """Print the last word popping it off."""
    word = words.pop(1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted word."""
    word = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    print_first_word(words)
    print_last_word(words)

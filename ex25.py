## Interestingly, the triple double quotes """ can be used without any initiation as a heading in themselves as this whole exercise shows. Second, the error in the exercise in splitting on null (changed it to splitting on " " to put the delimiters on words. Third, the function sorted() seems to run on lists (arrays?). Fourth, the function pop seems to pop out the n-th element of a list (array?). I'm not quite sure I understnad the difference between a list and an array right now. Also, to run a custom function - import into the context or "runtime", and call these functions as ex25.break_words("Mary had a little lamb")

## Beautiful other learning - naked """ """ strings are sent to help text. And, the title is important too -- wouldn't want to start the file with non-title stuff. Or, in fact, I could start the file with what we are intending to do. Wonder what conventions people follow on all these things. 

## One other thing that the pop function is doing - it is expelling the stated list element from the list itself. ['Mary, 'had', 'a', 'little', 'lamb'].pop(0) is getting rid of 'Mary'
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """Sorts the words"""
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    print(words)
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
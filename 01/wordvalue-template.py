from data import DICTIONARY, LETTER_SCORES

def load_words(dictionary):
    """Load dictionary into a list and return list"""
    with open(dictionary) as f:
        contents = f.read().split('\n')
    return contents

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter.upper()] for letter in word if letter.upper() in LETTER_SCORES.keys()])

def max_word_value(words=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_score = 0
    for word in words:
        if calc_word_value(word) > max_score:
            max_score = calc_word_value(word)
            max_word = word
    return max_word

def main():
    dictionary = load_words(DICTIONARY)
    max_word_value(dictionary)

if __name__ == "__main__":
    pass # run unittests to validate

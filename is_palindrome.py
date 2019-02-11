#!usr/bin/python


def is_palindrome(word: str='racecar'):
    """Returns boolean if a word is a palindrome."""

    word = word.strip().lower()
    reversed_word = ''.join(reversed(word))
    if word == reversed_word:
        return True
    else:
        return False

#!usr/bin/python

vowels = ('a', 'e', 'i', 'o', 'u')


def pig_latin(word: str='Python'):
    """Convert a word to pig latin."""

    word = word.strip().lower()
    prefix = ''
    for i in range(len(word)):

        # Check if the first letter is a vowel.
        if word[i] in vowels and i == 0:
            return word + 'ay'

        # Check if the first letter is a consonant.
        elif word[i] not in vowels and i == 0:
            prefix += word[i]

        # Check if the following letter(s) is a consonant.
        elif word[i] not in vowels and i != 0:
            prefix += word[i]

        # Check if the following letter(s) is a vowel.
        elif word[i] in vowels and i != 0:
            return str(word[len(prefix):] + prefix + 'ay').lower()

        # No logic needs to be applied.
        else:
            continue

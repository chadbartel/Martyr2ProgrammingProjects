#! usr/bin python


def count_vowels(word: str):
    """Returns the count of vowels in a word."""

    vowel_count = 0

    for i in range(len(word)):
        if word[i] in ('a', 'e', 'i', 'o', 'u'):
            vowel_count += 1
        else:
            continue

    return vowel_count

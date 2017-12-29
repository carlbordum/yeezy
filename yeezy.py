"""
    yeezy
    ~~~~~

    Password phrases generated with a Kanye West based markov chain.

    Example usage:
        $ yeezy 8
        he said man i feel like fuck it
"""

import sys
import random
import string
from collections import defaultdict


def clean_word(word):
    clean = []
    for char in word:
        char = char.lower()
        if char in string.ascii_lowercase:
            clean.append(char)
    return ''.join(clean)


def create_transition_table(words):
    table = defaultdict(list)
    for w0, w1, w2 in zip(words[0:], words[1:], words[2:]):
        table[w0, w1].append(w2)
    return table


def markov_chain(transition_table, length, w0, w1, w2):
    for __ in range(length):
        yield w2
        w0, w1, w2 = w1, w2, random.choice(transition_table[w1, w2])


if __name__ == '__main__':
    try:
        strength = int(sys.argv[1])
    except (IndexError, ValueError):
        print('Usage: yeezy LENGTH')
        sys.exit(1)
    with open('kanye_verses.txt') as f:
        words = list(map(clean_word, f.read().split()))

    transition_table = create_transition_table(words)
    i = random.randint(0, len(words)-3)
    print(' '.join(markov_chain(transition_table, strength, *words[i:i+3])))

import argparse
import random
import string

from itertools import cycle

vowels = 'aeiouy'
consonants = ''.join(c for c in string.ascii_lowercase if c not in vowels)

digraphs = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl',
            'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th',
            'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr',
            'squ', 'str', 'thr']
diphthongs = ['au', 'aw', 'ay', 'ea', 'ei', 'ew', 'oi', 'oo', 'ou', 'ow', 'oy']

_speedup = {char: tuple(part for part in digraphs + diphthongs if part.startswith(char))
           for char in vowels + consonants
           if any(map(char.startswith, digraphs + diphthongs))}

def pronounceable(length, digraph_chance=.5, diphthong_chance=.5):
    """
    Return a random, pronounceable word of length `length`.
    """
    word = ''
    char = random.choice(vowels + consonants)
    params = cycle(((consonants, digraph_chance), (vowels, diphthong_chance)))

    if char in consonants:
        next(params)

    while len(word) < length:
        word += char
        source, chance = next(params)
        char = random.choice(source)
        if char in _speedup and random.random() < chance:
            expansion = random.choice(_speedup[char])
            if len(word + expansion) < length:
                char = expansion

    return word


def main(argv=None):
    """
    Generate pronounceable words.
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('-n', type=int, default=1,
                        help='Number of words to generate. Default %(default)s')
    parser.add_argument('--length', type=int, default=5, help='Length of word. Default %(default)s')
    parser.add_argument('--digraph-chance', type=float, default=.5,
                        help='Chance to expand consonant into a random'
                             ' consonant digraph. Default: %(default)s')
    parser.add_argument('--diphthong-chance', type=float, default=.5,
                        help='Chance to expand diphthong into a random'
                             ' diphthong. Default: %(default)s')
    args = parser.parse_args()

    for _ in range(args.n):
        print(pronounceable(args.length, args.digraph_chance, args.diphthong_chance))

if __name__ == '__main__':
    main()

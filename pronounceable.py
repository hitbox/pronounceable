import argparse
import random
import string

vowels = 'aeiouy'
consonants = ''.join(c for c in string.ascii_lowercase if c not in vowels)
digraphs = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl',
            'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th',
            'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr',
            'squ', 'str', 'thr']
diphthongs = ['au', 'aw', 'ay', 'ea', 'ei', 'ew', 'oi', 'oo', 'ou', 'ow', 'oy']

def pronounceable(length, digraph_chance=.5, diphthong_chance=.5):
    """
    Return a random, pronounceable word of length `length`.
    """
    word = ''
    char = random.choice(vowels + consonants)
    while len(word) < length:
        word += char
        if char in vowels:
            char = random.choice(consonants)
            possible = tuple(digraph for digraph in digraphs if digraph.startswith(char))
            chance = diphthong_chance
        else:
            char = random.choice(vowels)
            possible = tuple(diphthong for diphthong in diphthongs if diphthong.startswith(char))
            chance = digraph_chance
        if random.random() < chance:
            if possible:
                expansion = random.choice(possible)
                if len(word + expansion) < length:
                    char = expansion
    return word


def main(argv=None):
    """
    Generate pronounceable words.
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--length', type=int, default=5, help='Length of word. Default %(default)s')
    parser.add_argument('--digraph-chance', type=float, default=.5,
                        help='Chance to expand consonant into a random'
                             ' consonant digraph. Default: %(default)s')
    parser.add_argument('--diphthong-chance', type=float, default=.5,
                        help='Chance to expand diphthong into a random'
                             ' diphthong. Default: %(default)s')
    args = parser.parse_args()
    print(pronounceable(args.length, args.digraph_chance, args.diphthong_chance))

if __name__ == '__main__':
    main()

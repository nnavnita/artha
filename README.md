# Artha
<img src="https://img.shields.io/badge/Python-3.9.8-brightgreen" />

A python model of the Sanskrit language.

## Abilities:

### Vyakarana (Grammar)
1. Decompose a Svara (alphabet)
```
python3 src au # svara processed but no output
python3 src au -pp # svara processed with prettified output
    Svara: au
    Kind: compound
    Breakdown: ['a', 'a', 'u']

python3 src A I U -pp # multiple svara processed with prettified output
    Svara: A
    Kind: long
    Breakdown: ['a', 'a']

    Svara: I
    Kind: long
    Breakdown: ['i', 'i']

    Svara: U
    Kind: long
    Breakdown: ['u', 'u']
```
2. Discover alphabet type
```
navnita@Navnitas-MacBook-Pro artha % python3 src -pp au kh aM
    Svara: au
    Kind: compound
    Breakdown: ['a', 'a', 'u']

    Alphabet: kh
    Kind: consonant

    Alphabet: aM
    Kind: anusvara
```
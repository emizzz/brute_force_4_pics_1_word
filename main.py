'''
                         ---BRUTE FORCE 4 PICS 1 WORD---
    A STUPID script that allows you to find a word in the game "4 Pics 1 Word".

'''

import csv
from progress import progress
from itertools import permutations

my_word = ""
length = 0
dataset = []
target = []

try:
    my_word = input("Write here the available characters (example: kacjucdvumuo): ")
    length = int(input("How long is the word? (example: 6): "))

    with open('dataset/english_words', newline='') as inputfile:
        for row in csv.reader(inputfile):
            dataset.append(row[0])

    perm = permutations(my_word, length)
    permLen = len(list(permutations(my_word, length)))

    for i, word in enumerate(list(perm)):
        progress(i+1, permLen, status='searching')
        word = ''.join(word)
        if word in dataset:
            target.append(word)

    print("\n")
    if len(target) > 0:
        print("Try one of the following words:")
        print(target)
    else:
        print("I can't find any word.")

except Exception as e:
    print("\n")
    print("Not valid input")








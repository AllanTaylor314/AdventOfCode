"""
Inspired by https://www.reddit.com/r/adventofcode/comments/zczgt4/2022_day_05_find_which_specific_letter_will_be_on/

You can modify an input to produce two distinct 9-letter Christmas words
(from https://wisforwebsite.com/christmas-words-by-number-of-letters/#Nine-Letter-Christmas-Words)

abc.txt is used to find out which positions end up on top
template.txt is filled in by this script to produce other "inputs"
"""

import os
from pathlib import Path
# Make sure we're working relative to this file, not the PWD
BASE_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
words = """
Ornaments
Snowflake
Gratitude
Unselfish
Bethlehem
Greetings
Fruitcake
Mincemeat
Mistletoe
Blessings
Fireplace
Snowbound
Tradition
Trimmings
Decorated
Incarnate
Innocence
Nostalgia
Partridge
Reverence
""".upper().split()
pairs = []
for word1 in words:
    for word2 in words:
        # Words that overlap in the right place
        if word1[4]==word2[0]:
            pairs.append((word1,word2))
with open(BASE_PATH/"template.txt") as file:
    header, instructions = file.read().split("\n\n")
# The lowercase letters in the header that end up on top
template="abcdzfghi"+"zklmnopqr"
for w1,w2 in pairs:
    new_header = header
    for a,b in zip(template,w1+w2):
        new_header = new_header.replace(a,b)
    print("###",w1,w2,"###")
    print(new_header)
    print("#"*26)
    with open(BASE_PATH / f"{w1}-{w2}.txt","w") as file:
        file.write(new_header)
        file.write("\n\n")
        file.write(instructions)

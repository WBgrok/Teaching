"""
Building a word count dictionary for a nursery rhyme.
https://www.w3schools.com/python/python_dictionaries.asp is a good primer on python dict syntax
"""

LYRIC = "One man went to mow, went to mow a meadow One man and his dog Went to mow a meadow Two men went to mow Went to mow a meadow Two men, one man and and his dog Went to mow a meadow Three men went to mow Went to mow a meadow Three men, two men, one man And his dog Went to mow a meadow Four men went to mow Went to mow a meadow Four men, three men, two men, one man And is dog Went to mow a meadow Five men went to mow Went to mow a meadow Five men, four men, three  men, two men, one man And his dog Went to mow a meadow Six men went to mow Went to mow a meadow Six men, five men, four men, three men, two men, one man And his dog Went to mow a meadow Seven men went to mow Went to mow a meadow Seven men, six men, five men, four men, three men, two men,  one man And his dog Went to mow a meadow Eight men went to mow Went to mow a meadow Eight men, seven men, six men, five men Four men, three men, two men, one man And his dog Went to mow a meadow"

# Make it into a list of strings:
WORDS = LYRIC.split(" ")

# lower the case
WORDS = list(map(str.lower, WORDS))

# strip commas
WORDS = [word.strip(',') for word in WORDS]

# create an empty dictionary
w_count = dict()


w_count["key"] = 12
"""
Task: write code so that w_count has each word in LYRIC as a key,
and for each of those, the value is the number of time the word appears.

Basic: you'll need a loop with a test in it
Pythonic: you can do this in one line with a dictionary comprehension (and list.count())
"""


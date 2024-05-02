import networkx as nx
import matplotlib.pyplot as plt
f = open("words.txt")
lines = f.readlines()
f.close()

WORDS = [w.strip() for w in lines]

ABET = list(map(chr, range(97,123)))
VWLS = ['a', 'e', 'i', 'o', 'u', 'y']

def is_word(w):
  return w in WORDS

def get_neighbours(w):
  neighbours =[]
  for i in range(len(w)):
    for l in ABET:
      c = w[:i] + l + w[i+1:]
      if c != w and is_word(c):
        # print(c)
        neighbours.append(c)

  return neighbours


"""
               Short-Bread: Graph exploration in practice

Short-Bread is a problem we used to set as an interview question. 

Given two words are neighbours if you can go from one to the other by changing a letter.
e.g. "short" connects to "shirt", "shoot", "snort", etc...

Find the path ( if exist) to go from "short" to "bread"

The interviewee would be expected to describe a graph traversal, ideally with a heuristic - not implement it.

Here, you will implement it. I'm using the Wordle dictionary of five letter english words

DO NOT TOUCH THE CODE BELOW
"""
# load up the dictionary

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
"""
END OF THE CODE YOU DO NOT TOUCH

With is_word and get_neighbour, you have enough to traverse the graph (you probably won't even need is_word)
"""

print(get_neighbours("bread"))

# You will need:

VISITED = [] # list of visited nodes
TO_VISIT = [] # list of nodes to visit.

# Python lists can be used as stacks or queues.
# To push or enqueue:
# TO_VISIT.append(node) #adds to the back

# But remember that get_neighbours returns a list - in practice, you'll be doing
# TO_VISIT.extend(neighbours)

# to pop:
# TO_VISIT.pop() # pops the last element

# to dequeue:
# TO_VISIT.pop(0) # pops the first element.


# Also, some heplful functional magic:
# TO_VISIT = list(filter(lambda x: x not in VISITED, TO_VISIT))
# This will remove from TO_VISIT any node (word) in VISITED - call this after adding to TO_VISIT

def find_bf(start, target):
  global TO_VISIT
  global VISITED
  VISITED.append(start)
  TO_VISIT.extend([ n for n in get_neighbours(start) if n not in TO_VISIT and n not in VISITED])
  print(TO_VISIT)
  while target not in TO_VISIT:
    current = TO_VISIT.pop(0)
    print(f"visiting {current}")
    VISITED.append(current)
    neighbours = list(filter(lambda x: x not in VISITED, get_neighbours(current)))
    TO_VISIT.extend(neighbours)
    # TO_VISIT.extend([n for n in neighbours if n not in TO_VISIT])
  if target in TO_VISIT:
    VISITED.append(target)
    print(VISITED)
    print(f"Target found! in {len(VISITED)} visits")

# find_bf("short", "skirt")
# find_bf("short", "whift")
find_bf("alice", "genes")
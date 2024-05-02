"""
not even OOP - but refactoring this as a Class is left as an exercise to the reader
"""


tree = [
  ['A', None, 1],
  ['S', 2, 4],
  ['L', 3, None ],
  ['E', None, None],
  ['T', None, None],
]


def printTree(tree, current = 0):
  if tree[current][1] is not None:
    printTree(tree, tree[current][1])
  print(tree[current][0], end=' ')
  if tree[current][2] is not None:
    printTree(tree, tree[current][2])

def printPreTree(tree, current = 0):
  # Implement this
  pass

def printPostTree(tree, current = 0):
  # Implement this
  pass

printTree(tree)
print()
# printPreTree(tree)
# printPostTree(tree)

def insert(tree, val, current=0):
  """STRETCH: Implement this
  Hint: https://parsons.problemsolving.io/puzzle/f1d8dba35b69449398cb7128cabf423c

  Write corresponding testing code
  """

insert(tree, 'C')
printTree(tree)
print(tree)
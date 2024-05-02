tree = [
  ['A', None, 1],
  ['S', 2, 4],
  ['L', 3, None ],
  ['E', None, None],
  ['T', None, None],
]

def insert(tree, val):
  tree.append([val, None, None])
  i_new = len(tree) - 1 
  inserted = False
  current = 0
  while not inserted:
    if val <= tree[current][0]:
      if tree[current][1] == None:
        tree[current][1] = i_new
        inserted = True
      else:
        current = tree[current][1]
    if val > tree[current][0]:
      if tree[current][2] == None:
        tree[current][2] = i_new
        inserted = True
      else:
        current = tree[current][2]

def printTree(tree, current = 0):
  if tree[current][1] is not None:
    printTree(tree, tree[current][1])
  print(tree[current][0])
  if tree[current][2] is not None:
    printTree(tree, tree[current][2])

def printPreTree(tree, current = 0):
  print(tree[current][0])
  if tree[current][1] is not None:
    printTree(tree, tree[current][1])
  if tree[current][2] is not None:
    printTree(tree, tree[current][2])

def printPostTree(tree, current = 0):
  print(tree[current][0])
  if tree[current][1] is not None:
    printTree(tree, tree[current][1])
  if tree[current][2] is not None:
    printTree(tree, tree[current][2])

printTree(tree)
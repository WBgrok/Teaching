class Tree:
  @staticmethod
  def balance(tree):
    # Will return a tree object that's the input tree, re-balanced
    out = Tree()
    l = tree.inOder()
    def r_balance(out, l):
      mid = len(l)//2
      out.insert(l[mid])
      r_balance(out, l[:mid-1])
      r_balance(out, l[mid:])
    r_balance(out, l)

  def __init__ (self, in_data = None):
    self.data = in_data
    self.left = None # this will ultimately contain another instance of Tree
    self.right = None

  """
  Insertion logic:
  This Tree class is really a Node class - a tree instance is a handle on the root node,
  with any children node composited into it. So I will use the term "node" in this description

  If there is no .data in the node, set .data to new_value, return
  Else:
    if the new value comes before the data in the node:
      if there is a a .left child
        use the insert method to insert the new value in the left sub-tree
      if there isn't
        instanciate a new node, set .left to it
    elif the new value comes after the data in the node
      same steps, but on the right subtree
    else (there is data in the node, and it's equal to the data we want to insert)
      return (we don't insert duplicates)
  """

  def insert (self, new_value):
    # I've done this for you, but for a challenge, wipe it and re-write it!
    if self.data is not None:
      if new_value < self.data:
          if self.left is not None:
            self.left.insert(new_value)
          else:
            self.left = Tree(new_value)
      elif new_value > self.data:
          if self.right is not None:
            self.right.insert(new_value)
          else:
            self.right = Tree(new_value)
      else:
        # We do not accept duplicate
        print("Already in tree")
        return
    else:
      self.data = new_value
      print("New node added")

  def inOder(self):
    l = self.left.inOrder() if self.left else []
    r = self.left.inOrder() if self.right else []
    return l + [self.data] + r


  def printTree(self):
    if self.left is not None:
      self.left.printTree()
    print(self.data, end = ' ')
    if self.right is not None:
      self.right.printTree()

  def printPreTree(self):
   # Implement this!
    pass

  def printPostTree(self):
    # Implement this!
    pass

  def display(self):
    pass

  def getElement(self, element):
   """
    Given an element, returns True if it is persent in the Tree,
    False otherwise

    Extension: instead of True, return the depth of an the element (consider the root to have depth zero)
   """

  def getDepth(self):
    """
      Returns the depth of the tree
    """



print ("==============================================")
print ("=== Loading tree with numbers ===")
theTree = Tree(50)
theTree.insert (30)
theTree.insert (20)
theTree.insert (40)
theTree.insert (10)
theTree.insert (80)
theTree.insert (100)
theTree.insert (60)
theTree.insert (70)
theTree.insert (90)
print ("\n=== In-order traversal of tree ===")
theTree.printTree ()
print ("\n=== Pre-order traversal of tree ===")
theTree.printPreTree ()
print ("\n=== Post-order traversal of tree ===")
theTree.printPostTree ()

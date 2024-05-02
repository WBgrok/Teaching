class Graph:
  """
  Implement this, it should have:
  Attributes
    nodes - list of nodes
    matrix - 2d data structure of Booleans
  Methods
    constuctor: accepts a list of nodes
    connect: accepts two nodes, connect them
    is_neighbour: takes two nodes, returns a Boolean if they're  directly connected.
  CHALLENGE:
    add_node(node): adds a node.
    is_connected(a, b): returns a Boolean if there is a path from a to b
    path(a,b): returns the a to be path as a list of nodes, or None if they're not connected
  
  """
  pass


g = Graph(["A", "B", "C"])
g.connect("A", "B")
g.is_connected("A", "C") # should return False
g.is_connected("A", "B") # should return True
g.is_connected("B", "A") # What should this return? Why?


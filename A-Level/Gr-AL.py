class Graph:
  """
  Implement this OVER A LIST , it should have:
  Attributes
    nodes - list of nodes
    list - dictionary, key is the node, value is the list of nodes connected to it
  Methods
    constuctor: accepts a list of nodes
    connect: accepts two nodes, connect them
    is_neighbour: takes two nodes, returns a Boolean if they're  directly connected.
    add_node(node): adds a node.
  CHALLENGE:
    remove_node(a): removes a from the graph
    sub_graph(a): returns a list of all nodes connected  to a, directly or indirectly 
    is_connected(a, b): returns a Boolean if there is a path from a to b
    path(a,b): returns the a to be path as a list of nodes, or None if they're not connected
  
  """
  def __init__(self, nodes):
    self.__list = {n: [] for n in nodes}
    print(self.__list)



  def connect(self, n1, n2):
    # Before: [ [] [] [] ]
    # After: [ ["B"] ["A"] []]
    self.__list[n1].append(n2)
    self.__list[n2].append(n1)


  def is_neighbour(self, n1,n2):

    return (n2 in self.__list[n1] and n1 in self.__list[n2])

  def add_node(self, n):
    pass



g = Graph(["A", "B", "C"])
g.connect("A", "B")
print(g.is_neighbour("A", "C")) # should return False
print(g.is_neighbour("A", "B")) # should return True
print(g.is_neighbour("B", "A")) # What should this return? Why?


class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.matrix = []
    for _ in nodes:
      self.matrix.append([False] * len(nodes))
    print(self.matrix)

  def connect(self, a, b):
    if (a not in self.nodes) or (b not in self.nodes):
      raise Exception
    # a and b are nodes
    ia = self.nodes.index(a)
    ib = self.nodes.index(b)
    self.matrix[ia][ib] = True
    print(self.matrix)

  def is_connected(self, a, b):
    if (a not in self.nodes) or (b not in self.nodes):
      raise Exception
    # a and b are nodes
    ia = self.nodes.index(a)
    ib = self.nodes.index(b)
    return self.matrix[ia][ib]

g = Graph(["A", "B", "C"])
g.connect("A", "B")

print(g.is_connected("A", "C")) # should return False
print(g.is_connected("A", "B")) # should return True
print(g.is_connected("B", "A")) # should return...

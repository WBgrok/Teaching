# We'll use list to represent expressions - assume the elements are either int or one-char operators ^/*+-
OPERATORS = ['+', '-', '*', '/']

example_expr = [1, 2, "+", 3, '*', 1, '+', 10, 10, '*', '-']

class Stack:
  """
    Implementation courtesy of GS, OP 23
    Needless to say, you should not need to change his excellent code.
  """

  def __init__(self):
    self._items = []
      
  def isEmpty(self):
    if self.size() > 0:
      return False
    else:
      return True
      
  def push(self, item):
    self._items.append(item)
      
  def pop(self):
    if not self.isEmpty():
      return self._items.pop(-1)
      
  def peek(self):
    if not self.isEmpty():
      return self._items[0]

  def size(self):
    return len(self._items)

s = Stack()

def eval_rpn(expression):
  global s
  for i in expression:
    if not i in OPERATORS:
      s.push(i)
      continue
    opr = i
    op1 = s.pop()
    op2 = s.pop()
    s.push(eval(f"{op2} {opr} {op1}"))
  return s.pop()
  
      
  

# Test
print(eval_rpn(example_expr)) # should return 9
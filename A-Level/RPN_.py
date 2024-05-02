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
  """
  Implement this.
  
  To avoid having lots of conditional logic to hanld the operations themselsves,
  build atomic infix expressions (Operand Operator Operand),
  then pass them to eval(): 
  eval("1 + 1") will return 2

  Also notice the test data has numbers as ints, not strings. You can
  solve this gracefully with f-strings: eval(f"{a} {op} {b}") 

  """
  s = Stack()

  
      
  

# Test
print(eval_rpn(example_expr)) # should return 9
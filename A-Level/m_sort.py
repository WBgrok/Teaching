import random

# DO NOT CHANGE THIS
# A list of random numbers (note the list comprehension)
l = [random.randint(1,2000) for _ in range(1024)]
print(l)


# Implement this!
def merge(l1: list[int], l2: list[int]) -> list[int]:
  """
  Arguments:
    l1, l2 are lists of ints, both sorted.
  Return:
    the merged, sorted list of l1 and l2
  """
  pass # don't forget to remove this :D

def sort(l: list[int]) -> list[int]:
  """
  Argument:
    l is an unsorted list of int
  Return
    the sorted list
  """
  pass
  # Think about how you would define this using only
  # the merge function and the sort function


# Testing
s = sort(l)
assert s == sorted(l)
print("if you see htis line, your code is sound")

"""
STRETCH
  1) write r_merge, which does the same as merge, but recursively
  2) now that your code doesn't use state and iteration, port it to Haskell (once we've seen it)
"""
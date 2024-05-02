import random

# DO NOT CHANGE THIS
# A list of random numbers (note the list comprehension)
l = [random.randint(1,2000) for _ in range(1024)]
# print(l)


# Implement this!
def merge(l1: list[int], l2: list[int]) -> list[int]:
  """
  Arguments:
    l1, l2 are lists of ints, both sorted.
  Return:
    the merged, sorted list of l1 and l2
  """
  # initialise an empty list (out)
  out = []
  while l1 and l2 :
    print(f"{l1}\n{l2}")
    #  if the head ([0]) of l1 is smaller than the head of l2:
    if l1[0] < l2[0]:
      out.append(l1[0])
      l1 = l1[1:]
    else:
      out.append(l2[0])
      l2 = l2[1:]
  
  return out

l1 = sorted([random.randint(1,100) for _ in range(4)])
l2 = sorted([random.randint(1,100) for _ in range(11)])

print("merge test")
print(merge(l1, l2))


  
  # then: append the head of l1 to the output list, remove the head from l1
  # else: same thing for l2


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
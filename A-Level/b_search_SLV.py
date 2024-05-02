import random

# DO NOT CHANGE THIS
# A sorted list of random numbers (note the list comprehension)
l = sorted([random.randint(1,2000) for _ in range(1024)])
# print(l)


# Implement this
def b_search(l: list[int], v: int) -> bool:
  """
  Arguments:
    l: list of int
    v: integer value
  Return:
    True/False depending on whether v is in l
  """
  
  found = False
  while not found:
    # print(len(l))
    if len(l) == 0:
      return False
    middle = len(l) // 2
    print("mid:", l[middle])
    if l[middle] == v:
      return True
    elif v < l[middle]:
      l = l[:middle]
    else:
      l = l[middle:]
    if len(l) == 1:
      return False


# Testing:
# t = [random.randint(1,2000) for _ in range(5)]
k = list(range(1,21))
b_search(k, 14)
# for v in t:
#   print(f"{v} in list: {b_search(l, v)}")


"""
STRETCH:
  1) return the index of v if it is in l, -1 otherwise
  2) write a recursive version (just returning True/False)
"""
# load up the dictionary

f = open("words.txt")
lines = f.readlines()
f.close()

WORDS = [w.strip() for w in lines]

ABET = list(map(chr, range(97,123)))
VWLS = ['a', 'e', 'i', 'o', 'u', 'y']

def is_word(w):
  return w in WORDS

def get_neighbours(w):
  neighbours =[]
  for i in range(len(w)):
    for l in ABET:
      c = w[:i] + l + w[i+1:]
      if c != w and is_word(c):
        # print(c)
        neighbours.append(c)

  return neighbours

def get_score(word, target):
  score = 0
  for i in range(len(target)):
    # 3 point per letter in place
    if word[i] == target[i]:
      score += 3
    if ((word[i] in VWLS) and (target[i] in VWLS)) or ((word[i] not in VWLS) and (target[i] not in VWLS)):
      # 1 point for consonant/vowel match
      score += 1
  return score

def get_weighted_neighbours(w, t):
  ns = get_neighbours(w)
  wns = list()
  for n in ns:
    wns.append([n, get_score(n, t)])
  return wns

def search(start, target):
  to_visit = [[start, 0]]
  visited =[]
  while to_visit:
    to_visit = sorted(to_visit, key=lambda x:x[1], reverse=True)
    current = to_visit.pop(0)
    print(f"current = {current}")
    print(f"visited = {visited}")
    if current[0] == target:
      return True
    visited.append(current)
    # neighbours = get_weighted_neighbours(current[0], target)
    # print([w for w in get_weighted_neighbours(current[0], target) if (w not in visited) and (w not in to_visit)] )
    to_visit.extend([w for w in get_weighted_neighbours(current[0], target) if(w not in to_visit) and (w not in visited)])
    print(f"to visit: {to_visit}")
    # input()
    
  # after the loop
  # to _visit is empty - we've explored the whole graph without finding the target
  return False

    
  

search('aahed', 'short')
# nbs = get_weighted_neighbours('short', 'bread')
# print(nbs)




      

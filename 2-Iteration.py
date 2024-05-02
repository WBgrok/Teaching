L = [0, 50, 100, 150, 200, 250, 300, 350, 400]

# There are two ways to iterate over L

#  "Foreach" Do something _for_ each element _in_ L:
for e in L:
    print(e)
print()
# "explicit iterator" Get an iterator* to go between 0 and 8 (because L has 9 elements) 
# (* an integer variable that increments - a counter)

# We do this using range: range(9) is [0,1,2,3,4,5,6,7,8]
# so the line below will have i take each of these values
for i in range(9):
    print(i)
print()
# we can then access elements of L via square brackets:
# also, instead of a hard-coded 9, len(L) will allow us to add/remove to L
for i in range(len(L)):
    print(L[i])
print()

"""
Comment out the code above with triple double-quotes (like this block) after you've run it.

Given the recap above, write some code to iterate over L,
printing each element, and the next one. 

Your code should print:
0 50
50 100
100 150
150 200
200 250
250 300
350 400

Note that this prints only 8 lines, not 9 like the previous ones.

Tip: Use the second type of for - explicit iterator
STRETCH: Can you make another version that uses the first type of iteration (foreach)?

"""

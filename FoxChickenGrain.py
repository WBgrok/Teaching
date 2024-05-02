# Fox, chicken, grain program
# https://time2code.today/python-course/python-fox-chicken-grain

# Output "A fox, chicken and bag of grain are on the North side of the river."

# Assign four variables: 'farmer', 'fox', 'chicken', and 'graim' to be "North"

# Ask the user to input their choice (any of the four words above) - store this in a variable 'choice'

"""
The output should now look like this:
(THIS MEAN DO NOT MOVE ON IF IT DOESN'T, FIX YOUR CODE)
A fox, chicken and a bag of grain wait by the side of a river.

Which item will you take in your rowboat to the other side?

fox, chicken, grain or farmer?

Choose:
"""

#Add the following logic - you should use BOOLEAN OPERATORS
# choice is farmer AND farmer is 'North', set farmer to be 'South'
# choice is fox AND farmer is 'North' AND fox is 'North', set them both to 'South'
# choice is chicken and farmer is 'North' and chicken is 'North', set them both to 'South'
# AND THE LAST ONE FOR THE GRAIN - BY NOW YOU SEE THE PATTERN

# Define a subprogram called output, that takes no parameter
# Output two lines: What is on the North side of the river, and what is on the South side.
"""
The output should now look like this
(THIS MEAN DO NOT MOVE ON IF IT DOESN'T, FIX YOUR CODE)
A fox, chicken and a bag of grain wait by the side of a river.

Which item will you take in your rowboat to the other side?

fox, chicken, grain or farmer?

Choose: chicken

———————–

This side of the river:

Fox

Grain



The other side of the river:

Farmer

Chicken

———————–
"""

# Define a subprogram (a predicate) called 'lost_game' that takes no parameter, but returns a Boolean
# if farmer is South when both chicken and fox are North, print "The fox ate the chicken"
# if farmer is South when both chcken and grain, print "The chicken got constipation from too much starch"
# return True if the game is lost, False if it is not
# YOU MAY NOTICE THIS ONLY TAKES CARE OF HALF THE PROBLEM - YOU WILL COMPLETE THIS LATER
"""
The output should now look like this:
A fox, chicken and a bag of grain wait by the side of a river.

Which item will you take in your rowboat to the other side?

fox, chicken, grain or farmer?

Choose: grain

———————–

This side of the river:

Fox

Chicken



The other side of the river:

Farmer

Grain

———————–

The fox ate the chicken.
"""

# We now need to handle the cases when the farmer moves back from South to North
# Add statements to the main program to allow the famer to move back - this should affect the value of the correspondig variables in the right (mirrored) way
# Add statements to 'lost_game' to check for animal eating stuff they shouldn't on the South bank when the farmer is North.


# define a predicate called 'won_game' that takes no parameters.
#   if fox, chicken and grain are all 'South', Print "You win! You can now go meet the maor of the village on the south side, bribe him with farm goods (and a fox), so he gets a bridge built between the banks. I mean come on!"
#   return True if the puzzle is solved, False if it isn't


# in the main program, wrap the code for each river crossing in a loop, so the puzzle continues until it's either won or lost
# make sure this main loop contains calls to the two predicates to check fro win/lose every time the farmer changes side


# Make it look professional
# Meaningful, lower case variable name
# sensible use of whitespace (look at where there are blank lines and how man of them)
# subprograms and main program clearly signified with comments
# subprograms have a comment explaining their purpose

# CHALLENGE

# I know some of you all will finish early, so you can get bonus points by REFACTORING you code
# refactoring means changing the inner working of the codes, whilst keeping its functional behaviour (what it does in the world) the same

# Here are suggestion to improve this program:
# instead of using four variables, use a list
# create a subprogram to take the user's choice - it should loop until it has received a valid input. It should also accept, for instance, fox, Fox, FOX or even fOx and recognise all as "fox"
# generalise the lost_game checks: Instead of having many test, simplify them as "the farmer is on one side and two things that can eat each other are on the other"- it's possible to do in much fewer lines.
# create sub-program that handles river crossing - it should be a single procedure for both crossing, intelligently flipping the state of variable based on user choice. 
# Watch out in that last one - you will need to either have you four vars as a list, or declare them as global within the function so code inside the function can affect values of variables outside of the function.



from p5 import *

def setup():
    COLOURS = ["black", "blue", "cyan", "white", "yellow", "orange", "red"]
    size(400,400)
    background(255)
    
    # build TWO list of y-coordinates:
    L_GAP = 50
    R_GAP = 75
    L_HEIGHTS = list(range(0, height+1, L_GAP))
    R_HEIGHTS = list(range(0, 2 * height, R_GAP))
    print(L_HEIGHTS)

    no_stroke()

    # Using the 2-iteration from the previous exercise, draw
    # rectangles down the canvas
    
    # Below is code for one rectangle - the inside of your loop
    # should have lines like those 
    fill(COLOURS[5]) # replace the 3 by an expresssion using i 
    quad(0, L_HEIGHTS[3], width, R_HEIGHTS[3], width, R_HEIGHTS[4], 0, L_HEIGHTS[4])

def draw():
    pass
    # STRETCH

    # Move all the code from setup in draw() - delete the 'pass'
    # (we're now doing this every frame)

    # rename the variables in lower case, as they are now variables, not constants

    # change it so that 
    # l_gap = max(1,int(mouse_x))
    # r_gap = max(1,int(mouse_y))

    # then detect which of those is the smallest
    # define the heights for that side (let's say it's R) normally (0 to height+1, in r_gaps)
    # define the heights for the other side so they go from 0 to l_gap * len(r_heights) + 1 - in steps of l_gap, obviously
    # this is to make sure the lists have the same length.

    #The drawing code stays the same

run()
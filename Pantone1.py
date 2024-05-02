from p5 import *

def setup():
    COLOURS = ["black", "blue", "cyan", "white", "yellow", "orange", "red"]
    # build a list of y-coordinates:
    HEIGHTS = list(range(0, 401, 50))
    print(HEIGHTS) 

    size(400,400)
    background(255)
    no_stroke()

    # Using the 2-iteration from the previous exercise, draw
    # rectangles down the canvas
    
    # Below is code for one rectangle - the inside of your loop
    # should have lines like those 
    fill(COLOURS[5]) # replace the 3 by an expresssion using i 
    quad(0, HEIGHTS[3], width, HEIGHTS[3], width, HEIGHTS[4], 0, HEIGHTS[4])
    

run()
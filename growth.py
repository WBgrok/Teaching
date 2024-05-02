from p5 import *
from random import random

todo = []
done = []
ODDS = 0.01

def setup():
  size(400, 400)
  background(255)

def draw():
  global todo
  global done
  if todo:
    p = todo.pop(0)
    p[2] += 1
    stroke(p[2])
    point(p[0], p[1])
    for y in [-1, 1]:
      for x in [-1, 1]:
        if random() < ODDS:
          if not ([int(p[0] + x), int(p[1] + y)] in [[n[0], n[1]] for n in todo + done]):
            todo.append([int(p[0] + x), int(p[1] + y), 0])
            # print("new")
    done.append(p)
  else:
    print(len(done))
    todo = done
    done = []


def mouse_pressed():
  global todo
  todo.append([int(mouse_x), int(mouse_y), 0])
  # print(len(todo + done))
  print(todo + done)
  

run()
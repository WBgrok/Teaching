from p5 import *

L_GAP = 30
R_GAP = 45
COLOURS = ["black", "blue", "cyan", "white", "yellow", "orange", "red"]
HCOLOURS = ["000000", "000080", "008080", "FFFFFF", "808000", "FF8000", "FF0000"]

def setup():
  size(1000, 600)
  noStroke()
  # stroke("A00000")
  
def draw():
  l0 = 0
  r0 = 0
  c = 0
  L_GAP = int(mouse_x) if mouse_x != 0 else 1
  R_GAP = int(mouse_y) if mouse_y != 0 else 1
  for l1, r1 in zip(range(0,height *2, L_GAP), range(0, height * 2, R_GAP)):
    fill(COLOURS[c % len(COLOURS)])
    quad(0, l0, width, r0, width, r1, 0, l1)
    l0, r0 = l1, r1
    c += 1

run()
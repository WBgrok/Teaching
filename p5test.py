from p5 import *
import random

"""
    Balls 
"""

class Ball():
    scale = 0.01
    spring = 0.0001
    friction = 0.05
    balls = []
    max_vel = 0
    
    
    def __init__(self, x, y, mass, vel0 = Vector(0, 0)):
        self.pos = Vector(x,y)
        self.mass = mass # float
        self.radius = sqrt(mass)
        self.vel = vel0 # Vector
        self.acc = Vector(0,0)
        Ball.balls.append(self)
    
    def move(self, force = Vector(0, 0)):
        self.acc = force.mult(self.mass)
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        # On Edge, bounce
        if (self.pos.x < self.radius) or (width - self.radius < self.pos.x):
            self.vel.x *= -1
    
        if (self.pos.y < self.radius) or (height - self.radius < self.pos.y):
            self.vel.y *= -1
        self.vel.mult(1 - Ball.friction)
        if self.vel.mag() > Ball.max_vel:
            Ball.max_vel = self.vel.mag()
        
    def render(self):
        fill(255 * sqrt(self.vel.mag() / Ball.max_vel))
        ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        
        
    def run(self):
        sumforce = Vector(0,0)
        
        # Collisions
        for other in [b for b in Ball.balls if b != self]:
            if Vector.dist(self.pos, other.pos) < self.radius + other.radius:
                background(127)
                angle = atan2(other.pos.y - self.pos.y, other.pos.x - self.pos.x)
                targetX = self.pos.x + cos(angle) * (self.radius + other.radius)
                targetY = self.pos.y + sin(angle) * (self.radius + other.radius)
                
                force = Vector((targetX - other.pos.x), (targetY - other.pos.y))
                force.mult(Ball.scale * Ball.spring)
                # other.move(force)
                # sumforce.add(force.mult(-1))
                other.vel.add(force)
                self.vel.sub(force)
        # Gravity
        for other in [b for b in Ball.balls if b != self]:
            d = Vector.dist(self.pos, other.pos)
            # if 0 < d < self. radius * 10:
            force = Vector.sub(other.pos, self.pos)
            force.normalize()
            force.mult(Ball.scale * (self.mass + other.mass) / d)
            sumforce.add(force)
        
        self.move(sumforce)
        # self.render()

def mouse_pressed():
    Ball(mouse_x, mouse_y, random.randint(10,50), Vector(random.randint(-10, 10), random.randint(-10, 10)))
    
def key_pressed():
    Ball.balls.pop()

def setup():
    size(800, 600)
    noStroke()
    ellipseMode(RADIUS)
    
def draw():
    # background(127)
    Ball.max_vel = 0 
    for b in Ball.balls:
        b.run()
    for b in Ball.balls:
        b.render()

run()
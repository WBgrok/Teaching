from p5 import *

n=0
power = 1
n_clickers = 0
p_power = 10
p_clicker = 100 

def setup():    
    size(400, 400)
    background(0)
    text_align(LEFT, TOP)
    text_font(create_font("C:\Windows\Fonts\Arial.ttf", 16,))
    text_size(20)
    
def draw():
    global n
    background(0)
    fill(255)
    text(f"you have {n}.", 50, 10)
    if n_clickers:
        text(f"you have {n_clickers} clickers", 50, 40)
    if n >= p_power:
        disp_power()
    if n >= p_clicker:
        disp_clicker()
    n += n_clickers
        
def disp_power():
    msg=f"Increase click power (cost: {p_power})"
    stroke(255)
    fill(50,50,140)
    rect(50, 350, text_width(msg), 22)
    fill(255)
    text(msg, 50, 350)
    
def disp_clicker():
    msg = f"Buy auto-clicker (cost: {p_clicker})"
    stroke(255)
    fill(50,50,140)
    rect(50, 300, text_width(msg), 22)
    fill(255)
    text(msg, 50, 300)

def mouse_pressed():
    global n, power, p_power, p_clicker, n_clickers
    if n >= p_power and 50 < mouse_x < 350 and 350 < mouse_y < 372:
        #buying power
        n -= p_power
        power += 1
        p_power += 1
    elif n >= p_clicker and 50 < mouse_x < 350 and 300 < mouse_y < 322:
        # buying clicker
        n -= p_clicker
        n_clickers += 1
        p_clicker += 10
    else:
        n+= power


run()
# while True:
#     if n>=p_power:
#         print(f"Enter p to increase your tapping power (costs{p_power})")
    
#     print(f"you have tapped {n} times. Tap return for more.")
#     choice = input().upper()
#     if choice == 'P':
#         power += 1
#         n -= p_power
#         p_power += 1
    
#     n+=power
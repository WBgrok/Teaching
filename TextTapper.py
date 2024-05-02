import time

start = time.time()
prev = start
n = 0

while True:
  t = time.time()
  print("  ==Text Tapper==  ")
  print()
  print(f"Total time: {t-start}" )
  print(f"Total taps: {n}")
  if t > start:
    print(f"Lifetime TpS: {n / (t- start)}")
  choice = input()
  n += 1
  print("\033[H\033[J", end="")

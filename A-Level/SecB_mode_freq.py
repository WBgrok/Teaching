# read N - numdigits
N = int(input("Number of digits? "))

# initialise a frequency list.
freqs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# read N digits, incrementing the relevant item in freq
mode = 0
mm = False
for i in range(N):
  d = int(input(f"digit #{i}: "))
  freqs[d] = freqs[d] + 1
  if freqs[d] > mode:
    mm = False
    mode = freqs[d]
  elif freqs[d] == mode:
    mm = True

# display the largest count / multimodal
if mm:
  print("data was multimodal")
else:
  print("modal frequency:", mode)

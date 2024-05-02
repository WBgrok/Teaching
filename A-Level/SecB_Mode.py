N = int(input("Number of digits: "))
freq = [0] * 10
for _ in range(N):
    n = int(input("digit? "))
    if 0 <= n <=9:
        freq[n] += 1

i_max = -1
max = -1
for i in range(10):
    if freq[i] > max:
        max = freq[i]
        i_max = 1
    elif freq[i] == max:
        print("Data was multimodal")
print(f"Most entered digit: {i_max}")
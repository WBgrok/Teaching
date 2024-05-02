def gen_clltz(n):
  out = [n]
  while n != 1:
    n = n // 2 if n % 2 == 0 else n * 3 + 1
    out.append(n)
  return list(reversed(out))

d = [gen_clltz(n) for n in range(1,151)]


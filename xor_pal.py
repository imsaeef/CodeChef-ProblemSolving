t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(str, input().split()))[:n]
  s = ''.join(a)
  count = 0
  for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
      count += 1
  print((count + 1) // 2)
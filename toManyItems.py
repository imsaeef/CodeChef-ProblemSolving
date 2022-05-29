import math

t = int(input())
for _ in range(t):
    n = int(input())
    total_bag = n/10
    print(math.ceil(total_bag))
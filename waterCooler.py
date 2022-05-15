t = int(input())
for _ in range(t):
    x, y, m = map(int, (input().split()))
    print("yes" if x*m < y else "no")
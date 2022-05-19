t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    op = z - (y//x)
    print(max(0,op))
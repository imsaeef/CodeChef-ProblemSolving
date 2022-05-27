t = int(input())
for _ in range(t):
    x, y, d = map(int, input().split())
    if (x-y) <= d and (y-x) <= d:
        print('yes')
    else:
        print('no')
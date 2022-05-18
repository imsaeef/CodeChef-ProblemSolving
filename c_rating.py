t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    count = 0
    if x==y:
        print(0)
    else:
        for _ in range(y):
            x = x + 8
            count += 1
            if x>=y:
                break
        print(count)

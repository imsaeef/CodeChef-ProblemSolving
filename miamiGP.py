t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x*1.07 >= y:
        print("YES")
    else:
        print("NO")
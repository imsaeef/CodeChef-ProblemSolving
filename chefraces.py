t = int(input())
for _ in range(t):
    x,y,a,b = map(int, input().split())
    c = {x, y}
    r = {a, b}
    print(len(c-r))
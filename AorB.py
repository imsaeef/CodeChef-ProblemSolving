t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    A = 500 - (x*2)
    B = 1000 - (y*4)
    s1 = 500 - ((x+y) * 2)
    s2 = 1000 - ((x+y) * 4)
    f1 = A + s2
    f2 = B + s1

    if (f1) >= (f2):
        print(f1)
    else:
        print(f2)
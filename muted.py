t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    x_list = list(map(int, input().split()))
    c = 0
    for i in x_list:
        if (i+k)%7 == 0:
            c += 1
    print(c)
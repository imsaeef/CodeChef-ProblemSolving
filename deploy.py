for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))[:n]
    e = 0
    for i in range(n-1, 0, -1):
        if (x[i] != 0):
            e = i
            break
    print(e)
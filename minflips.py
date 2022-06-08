for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    if n%2 == 1:
        print(-1)
    else:
        if sum(a)==0:
            print(0)
        elif sum(a) < 0:
            print(abs(int(sum(a)/2)))
        else:
            print(int(sum(a)/2))
for t in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    if sorted(d) == d:
        print("yes")
    else:
        print("no")
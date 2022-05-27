for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for item in a:
        if item >= 10 and item <= 60:
            count += 1
    print(count)
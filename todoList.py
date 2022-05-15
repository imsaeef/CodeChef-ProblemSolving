t = int(input())
for _ in range(t):
    n = int(input())
    lists = list(map(int, input().split()))[:n]
    count = 0
    for i in lists:
        if i >= 1000:
            count += 1
    print(count)
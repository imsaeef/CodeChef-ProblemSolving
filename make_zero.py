t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    dish = 0
    for i in range(n):
        dish = dish | a[i]
        result = bin(dish)
    print(result.count('1'))
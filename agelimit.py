for _ in range(int(input())):
    x,y,a = map(int, input().split())
    print('YES' if a >= x and a < y else 'NO')
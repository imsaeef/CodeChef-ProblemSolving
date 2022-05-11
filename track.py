t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a>b:
        print(min(a-b, c-a+b))
    else:
        print(min(b-a, a+c-b))
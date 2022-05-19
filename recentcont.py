t = int(input())
for _ in range(t):
    s = 0
    l = 0
    n = int(input())
    n_list = list(map(str, input().split()))
    for i in range(0, n):
        if n_list[i] == "START38":
            s += 1
        else:
            l += 1
    print(s, l)
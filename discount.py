for t in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    s = sum(a)
    b = []
    for i in a:
        if i > y:
            b.append(abs(i - y))
        else:
            b.append(0)
    c = sum(b)
    d = x + c
    if d < s:
        print("coupon")
    else:
        print("no coupon")
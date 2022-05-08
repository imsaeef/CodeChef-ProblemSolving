t = int(input())
for _ in range(t):
    n,x,p = map(int,input().split())
    if ((x*3)-(n-x)) >= p:
        print("PASS")
    else:
        print("FAIL")

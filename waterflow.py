t = int(input())
for _ in range(t):
    w,x,y,z = map(int, input().split())
    result = w+y * z
    if result > x:
        print("overflow")
    elif result == x:
        print("filled")
    else:
        print("unfilled")
for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2 or n ==3 or n == 4:
        print(1)
    elif n == 5:
        print(2)
    else:
        n -= 1
        sm = (n//5) * 2
        n %= 5
        if n == 0:
            print(sm)
        elif n == 1 or n == 2 or n == 3:
            print(sm + 1)
        else:
            print(sm + 2)
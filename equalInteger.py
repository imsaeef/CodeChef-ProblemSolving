for t in range(int(input())):
    x,y = map(int, input().split())
    if x==y: print(0)
    else:
        if x<y: print(y-x)
        else:
            if x%2==0 and y%2==0 or x%2!=0 and y%2!=0: print((x-y)//2)
            else: 
                if x%2!=0 and y%2==0 or x%2==0 and y%2!=0: print(((x+1-y)//2)+1)
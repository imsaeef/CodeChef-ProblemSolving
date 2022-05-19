t = int(input())
for _ in range(t):
    x = int(input())
    if x%3 == 0:
        print("normal")
    elif x%3 == 1:
        print("huge")
    else:
        print("small")
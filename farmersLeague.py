t = int(input())
for _ in range(t):
    n = int(input())
    f_team = 3*(n-1)
    l_team = 3*((n-1)//2)
    print(f_team-l_team)
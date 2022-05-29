R, O, C = map(int, input().split())
played = 20-O #already played this over
per_over = played*6 #per ball max 6 run
per_over_run = per_over*6 #highest run for each over
possible_run = per_over_run+C #they can achive this run max
#lets find winners!
if possible_run > R:
    print("YES")
else:
    print("NO")
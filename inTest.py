n, k = map(int, input().split())
ans = 0
for _ in range(n):
    t = int(input())
    if t % k == 0:
        ans += 1
print(ans)
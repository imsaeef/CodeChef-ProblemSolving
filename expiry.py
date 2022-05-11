t = int(input())
for _ in range(t):
	n, m, k = map(int, input().split())
	print("Yes" if m*k >= n else "No")
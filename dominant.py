t = int(input())
for _ in range(t):
	nA, nB, nC = map(int, input().split())
	if nA > nB+nC or nB > nA+nC or nC > nA+nB:
		print("YES")
	else:
		print("NO")
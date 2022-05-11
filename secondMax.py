t = int(input())
for _ in range(t):
	n1, n2, n3 = map(int, input().split())
	#first method
	ans = sorted([n1, n2, n3])
	print(ans[1])
	#second method
	# if (n1>n2 and n1<n3) or (n1<n2 and n1>n3):
	# 	print(n1)
	# elif (n2>n1 and n2<n3) or (n2<n1 and n2>n3):
	# 	print(n2)
	# else:
	# 	print(n3)
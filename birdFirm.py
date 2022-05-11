t = int(input())
for _ in range(t):
	x, y, z = map(int, input().split())
	if z%x == 0 and z%y != 0:
		print("CHICKEN")
	elif z%x != 0 and z%y == 0:
		print("DUCK")
	elif z%x == 0 and z%y == 0:
		print("ANY")
	else:
		print("NONE")
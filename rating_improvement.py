for _ in range(int(input())):
  x,y = map(int, input().split())
  if x <= y and x+200 >= y: print('yes')
  else: print('no')
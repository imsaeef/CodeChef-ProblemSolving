# t = int(input())
# for _ in range(t):
#     x, y = map(int, input().split())
#     if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
#         print('janmansh')
#     else:
#         print('jay')

# second method
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if (x+y)%2 == 0:
        print('janmansh')
    else:
        print('jay')
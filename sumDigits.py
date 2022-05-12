# t = int(input())
# for _ in range(t):
#     n = int(input())
#     store = 0
#     while n > 0:
#         store = store + n % 10
#         n = n // 10
#     print(store)

#another method
t = int(input())
for _ in range(t):
    n = input()
    store = 0
    for item in n:
        store = store + int(item)
    print(store)
x, y = map(int, input().split())
spent_time = y/2
watch_time = x - y
total_time = spent_time + watch_time
print(round(total_time))
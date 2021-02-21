num = int(input())
road_length = times = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
ma = 1000000000

for i in range(num-1):
  if i == 0:
    total += price[0]*road_length[0]
    mi = min(price[i], ma)
  else:
    mi = min(price[i], mi)
    total += mi*road_length[i]
print(total)
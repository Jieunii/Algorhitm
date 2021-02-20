Num = int(input())
times = list(map(int, input().split()))
times.sort()
time, pre = times[0], 0

for i in range(1, len(times)):
  pre += times[i-1]
  time += (times[i]+pre)

print(time)
Num = int(input())
time = []

for i in range(Num):
  start, end = map(int, input().split())
  time.append([start, end])
time.sort(key=lambda x:(x[1], x[0]))

cnt = 1
s, e = time.pop(0)

while time:
  s1, e1 = time.pop(0)
  if e <= s1:
    cnt += 1
    s, e = s1, e1

print(cnt)
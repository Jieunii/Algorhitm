N, K = map(int, input().split())
value = []
cnt = 0

for i in range(N):
  value.append(int(input()))
value.reverse()

for money in value:
  if money <= K:
    num = K // money
    cnt += num
    K -= (num*money)

print(cnt)

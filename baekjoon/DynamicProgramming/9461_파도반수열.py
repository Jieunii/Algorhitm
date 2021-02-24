N = int(input())
test = []
dp = [0]*101

for i in range(N):
  test.append(int(input()))

dp[1] = 1
dp[2] = 1
dp[3] = 1

for t in test:
  for i in range(4, t+1):
    dp[i] = dp[i-2] + dp[i-3]
  print(dp[t])
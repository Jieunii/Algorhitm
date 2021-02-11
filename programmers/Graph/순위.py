from collections import defaultdict

def solution(n, results):
  win, lose = {}, {}
  win = defaultdict(set)
  lose = defaultdict(set)
  
  for i in range(1, n+1):
    for node1, node2 in results:
      if node1 == i:
        win[node1].add(node2)
      if node2 == i:
        lose[node2].add(node1)
    for winner in lose[i]:
      win[winner].update(win[i])
    for loser in win[i]:
      lose[loser].update(lose[i])
  
  cnt = 0
  for i in range(1, n+1):
    if len(win[i]) + len(lose[i]) == n-1:
      cnt += 1
  return cnt
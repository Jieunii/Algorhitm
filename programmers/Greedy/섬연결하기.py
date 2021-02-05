def solution(n, costs):
  answer = 0
  visited = [0]*n
  visited[0] = 1
  costs.sort(key=lambda x:x[2])
  
  while sum(visited) != n:
    for cost in costs:
      s, e, c = cost
      if visited[s] or visited[e]:
        if visited[s] and visited[e]:
          continue
        else:
          visited[s] = 1
          visited[e] = 1
          answer += c
          break
            
  return answer
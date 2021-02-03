answer = 0
def dfs(begin, target, words, visited):
  global answer
  stacks = [begin]
  while stacks:
    stack = stacks.pop()
    if stack == target:
      return answer
    for w in range(0, len(words)):
      if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:
        if visited[w] != 0:
          continue
        visited[w] = 1
        stacks.append(words[w])
    answer += 1

def solution(begin, target, words):
  global answer
  visited = [0]*len(words)
  if target not in words:
    return 0
  dfs(begin, target, words, visited)

  return answer
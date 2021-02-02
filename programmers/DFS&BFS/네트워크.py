# 1. 탐색을 위한 큐, 방문한 노드 체크 -> 리스트 2개
# 2. 탐색 시작할 노드 큐에 넣기
# 3. 큐 빌때까지
# 3-1. 큐 꺼내기
# 3-2. 꺼낸 노드에 인접한 노드 방문(반복문) -> 방문한 노드 이전에 방문한 적 없다면 큐에 넣고 방문 체크
def solution(n, computers):
  answer = 0
  bfs = []
  visit = [0]*n

  while 0 in visit:
    bfs.append(visit.index(0))
    visit[0] = 1
    while bfs:
      node = bfs.pop(0)
      for i in range(n):
        if visit[i] == 0 and computers[node][i] == 1:
          bfs.append(i)
          visit[i] = 1
    answer += 1
  return answer
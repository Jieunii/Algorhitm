def solution(tickets):
  tickets.sort(reverse=True)
  routes = dict()
  for x, y in tickets:
    if x in routes:
      routes[x].append(y)
    else:
      routes[x] = [y]
          
  stack = ["ICN"]
  answer = []
  while stack:
    top = stack[-1]
    if top not in routes or len(routes[top]) == 0:
      answer.append(stack.pop())
    else:
      stack.append(routes[top].pop())
  answer.reverse()
  return answer
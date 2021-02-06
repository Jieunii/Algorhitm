# 1
def solution(routes):
  answer = 0
  routes.sort()
  standard = routes[0][1]
  routes = routes[1:]
  answer += 1
  
  for route in routes:
    if route[0] <= standard:
      standard = min(route[1], standard)
    else:
      standard = route[1]
      answer += 1
  return answer

# 2
def solution(routes):
  answer = 0
  routes = sorted(routes, key=lambda x: x[1])
  camera = -30000

  for route in routes:
    if camera < route[0]:
      answer += 1
      camera = route[1]

  return answer
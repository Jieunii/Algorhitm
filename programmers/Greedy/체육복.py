# 1
def solution(n, lost, reserve):
  answer = n - len(lost)
  pro = lost.copy()
  while pro:
    pop = pro.pop(0)
    if pop in reserve:
      reserve.remove(pop)
      lost.remove(pop)
      answer += 1
  for i in lost:
      if i-1 in reserve:
        reserve.remove(i-1)
        answer += 1
      elif i+1 in reserve:
        reserve.remove(i+1)
        answer += 1

  return answer

# 2
def solution(n, lost, reserve):
  Reserve = [r for r in reserve if r not in lost]
  Lost = [l for l in lost if l not in reserve]
  answer = n - len(Lost)
  for i in Lost:
    if i-1 in Reserve:
      Reserve.remove(i-1)
      answer += 1
    elif i+1 in Reserve:
      Reserve.remove(i+1)
      answer += 1
            
    return answer
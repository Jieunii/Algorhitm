# 1
def solution(dartResult):
  answer = 0
  flag = -1
  d = [0, 0, 0]
  for idx, dart in enumerate(dartResult):
    if dart.isdigit():
      flag += 1
      if dart == '0':
        continue
      elif dartResult[idx+1].isdigit(): # 10일때
        d[flag] += 10
        flag -= 1
      else:
        d[flag] += int(dart)
    elif dart in 'SDT':
      if dart == 'D':
        d[flag] **= 2
      elif dart == 'T':
        d[flag] **= 3
      else:
        continue
    else:
      if dart == '*':
        d[flag-1] *= 2
        d[flag] *= 2
      else:
        d[flag] *= -1
  return sum(d)

# 2
import re

def solution(dartResult):
  bonus = {'S' : 1, 'D' : 2, 'T' : 3}
  option = {'' : 1, '*' : 2, '#' : -1}
  p = re.compile('(\d+)([SDT])([*#]?)')
  dart = p.findall(dartResult)
  
  for i in range(len(dart)):
    if dart[i][2] == '*' and i > 0:
      dart[i-1] *= 2
    dart[i] = int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
      
  answer = sum(dart)
  return answer
def solution(distance, rocks, n):
  answer = 0
  rocks.sort()
  rocks.append(distance)
  left, right = 0, distance
  
  while left <= right:
    pre = 0
    remove = 0
    mid = (left+right)//2
    mins = 10000000001
    
    for i in range(len(rocks)):
      if rocks[i] - pre < mid:
        remove += 1
      else:
        mins = min(mins, rocks[i] - pre)
        pre = rocks[i]
    if remove > n:
      right = mid - 1
    else:
      answer = mins
      left = mid + 1
  return answer
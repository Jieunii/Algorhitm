def solution(people, limit):
  start, end = 0, len(people)-1
  answer = 0
  people.sort(reverse=True)
  
  while start <= end:
    answer += 1
    if people[start] + people[end] <= limit:
      end -= 1
    start += 1
        
  return answer
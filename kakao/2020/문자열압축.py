def solution(s):
  length = []
  
  if len(s) == 1:
    return 1
  for cut in range(1, len(s)//2+1):
    answer = ""
    count = 1
    string = s[:cut]
    for i in range(cut, len(s), cut):
      if s[i:i+cut] == string:
        count += 1
      else:
        if count == 1:
          count = ""
        answer += str(count)+string
        string = s[i:i+cut]
        count = 1
    if count == 1:
      count = ""
    answer += str(count)+string
    length.append(len(answer))
  return min(length)
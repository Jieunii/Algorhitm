# 1
def solution(n, arr1, arr2):
  answer = []
  arr1 = list(map(lambda x: format(x,'0b'),arr1))
  arr2 = list(map(lambda x: format(x,'0b'),arr2))
  

  for i in range(n):
    if len(arr1[i]) != n or len(arr2[i]) != n:
      while len(arr1[i]) < n:
        arr1[i] = '0'+arr1[i]
      while len(arr2[i]) < n:
        arr2[i] = '0'+arr2[i]
              
  for i in range(n):
    secret = ''
    for j in range(n):
      if int(arr1[i][j]) | int(arr2[i][j]) == 1:
        secret += '#'
      else:
        secret += ' '
    answer.append(secret)

  return answer

# 2
def solution(n, arr1, arr2):
  answer = []
  secret = ''
  for i, j in zip(arr1, arr2):
    secret = str(bin(i|j)[2:])
    secret = secret.rjust(n, "0")
    secret = secret.replace("1", "#")
    secret = secret.replace("0", " ")
    answer.append(secret)
  return answer
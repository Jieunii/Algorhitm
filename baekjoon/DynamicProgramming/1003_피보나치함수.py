num = int(input())

while num:
  zero = [1, 0]
  one = [0, 1]
  t = int(input())
  
  for i in range(2, t+1):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])
  
  print(zero[t], one[t])
  num -= 1
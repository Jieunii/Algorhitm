n = int(input())
instruction = []
stack = []

for i in range(n):
  instruction.append(input())

for i in range(n):
  if 'push' in instruction[i]:
    a = instruction[i].split(' ')
    stack.append(int(a[1]))
  elif 'pop' == instruction[i]:
    if len(stack) != 0:
      print(stack.pop())
    else:
      print(-1)
  elif 'size' == instruction[i]:
    print(len(stack))
  elif 'empty' == instruction[i]:
    if len(stack) != 0:
      print(0)
    else:
      print(1)
  else:
    if len(stack) != 0:
      print(stack[-1])
    else:
      print(-1)
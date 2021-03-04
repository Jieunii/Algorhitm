n = int(input())
PS = []

def VPS(p):
  vps = []
  for j in range(len(p)):
    if p[j] == '(':
      vps.append(p[j])
    else:
      if not vps:
        print('NO')
        return
      else:
        vps.pop()
  if not vps:
    print('YES')
    return
  else:
    print('NO')
    return

for i in range(n):
  VPS(input())
expression = input().split('-')
result = []

for e in expression:
  minus = list(map(int, e.split('+')))
  result.append(sum(minus))

for r in result[1:]:
  result[0] -= r
print(result[0])
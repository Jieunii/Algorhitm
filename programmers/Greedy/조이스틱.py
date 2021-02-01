# 상하로 최소 & 좌우로 최소(A가 아닌 거 더 빨리 만나기)
def solution(name):
  idx, answer = 0, 0
  updown = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]

  while(True):
    answer += updown[idx]
    updown[idx] = 0
    if sum(updown) == 0:
      break
    left, right = 1, 1
    while updown[idx - left] == 0:
      left += 1
    while updown[idx + right] == 0:
      right += 1
    answer += left if left < right else right
    idx += -left if left < right else right
  return answer
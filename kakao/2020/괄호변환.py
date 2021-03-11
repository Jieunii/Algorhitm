def divide(w):
    left = right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = w[:i+1]
            v = w[i+1:]
            return u, v

def checkCorrect(w):
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            stack.append(w[i])
        else:
            if not stack:
                return False
            stack.pop()        
    return True

def solution(p):
    answer = ''

    if len(p) == 0:
        return ""
    u, v = divide(p)

    if checkCorrect(u):
        answer = u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:len(u)-1]
        for i in range(len(u)):
            if u[i] == ')':
                answer += '('
            else:
                answer += ')'
    return answer
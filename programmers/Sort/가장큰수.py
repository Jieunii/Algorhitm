def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
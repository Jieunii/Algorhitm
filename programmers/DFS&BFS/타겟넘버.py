def solution(numbers, target):
    answers = [0]

    for n in numbers:
        new_answers = []
        for a in answers:
            new_answers.append(a + n)
            new_answers.append(a - n)
        answers = new_answers

    return answers.count(target)
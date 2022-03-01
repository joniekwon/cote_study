def solution(n):
    answer = [0, 1] + [0] * (n - 1)
    for i in range(2, len(answer)):
        answer[i] = (answer[i - 2] + answer[i - 1]) % 1234567
    return (answer[-1])

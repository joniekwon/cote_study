def solution(s):
    answer = []
    for i in s:
        if len(answer)<1:
            answer.append(i)
            continue
        if i==answer[-1]:
            answer.pop()
        else:
            answer.append(i)

    if len(answer)>=1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    s='baabaa'
    print(solution(s))
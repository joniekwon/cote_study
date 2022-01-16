def solution(dartResult):
    area = ['S', 'D', 'T', '*', '#']
    answer = []
    temp = ''
    for s in dartResult:
        if s not in area:
            temp += s
        else:
            if temp != '':
                answer.append(int(temp))
                temp = ''
            if s=='D':
                answer[-1] = pow(answer[-1], 2)
            elif s=='T':
                answer[-1] = pow(answer[-1], 3)
            elif s=='*':
                answer[-1] *= 2
                if len(answer) > 1:
                    answer[-2] *= 2
            elif s=='#':
                answer[-1] *= -1
    return sum(answer)


if __name__ == '__main__':
    dartResult = '1S2D*3T'
    print(solution(dartResult))
from string import ascii_letters
def solution(s, n):
    alpha = [s for s in ascii_letters]

    answer = ''
    for x in s:
        if x == ' ':
            answer += ' '
        elif x.islower():
            answer += alpha[(alpha.index(x)+n)%(len(alpha)//2)]
        else:
            answer += alpha[(len(alpha)//2)+(alpha.index(x)+n)%(len(alpha)//2)]
    return answer



if __name__ == "__main__":
    s = 'AB'
    n = 1
    print(solution(s, n))

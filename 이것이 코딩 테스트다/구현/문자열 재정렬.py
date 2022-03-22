# 알파벳 대문자와 숫자0~9로만 구성된 문자열이 주어집니다.
#모든 알파벳을 오름차순으로 정렬하여 이어 출력한 뒤에 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
def solution(S):
    answer = ''
    n = 0
    for x in S:
        if x.isdigit():
            n+=int(x)
        else:
            answer+=x
    answer = ''.join(sorted(answer)) + str(n)
    return answer

if __name__=='__main__':
    S = ['K1KA5CB7', 'AJKDLSI412K4JSJ9D']
    for s in S:
        print(solution(s))

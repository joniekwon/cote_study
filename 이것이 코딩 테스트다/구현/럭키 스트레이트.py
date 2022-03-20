# 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황인지 아닌지
# 동일하다면 "LUCKY" 동일하지 않다면 "READY"를 출력
def solution(score):
    l = len(score)//2
    left = 0; right = 0
    for i, s in enumerate(str(score)):
        if i < l:
            left+=int(s)
        else:
            right+=int(s)

    return 'LUCKY' if left==right else "READY"


if __name__ == '__main__':
    score = '7755'
    print(solution(score))
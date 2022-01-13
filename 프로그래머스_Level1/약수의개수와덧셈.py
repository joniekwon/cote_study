
# 제곱근으로 나누어떨어지는 숫자는 약수가 홀수, 아니면 짝수임을 이용
def solution(left, right):
    answer=0
    for i in range(left, right+1):
        if int(i**0.5)**2 == i:
            answer-=i
        else:
            answer+=i
    return answer

if __name__ == '__main__':
    print(solution(13,17))
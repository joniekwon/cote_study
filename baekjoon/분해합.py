n = int(input())

l = len(str(n))
answer = False
# 각 자리가 모두 9일 경우가 있을 수 있으므로 범위는 n - length*9 ~ n+ length*9로 설정하여 탐색
for i in range(n-9*l, n+9*l):
    s = 0
    number=i
    # 각 자리수마다 더해주고 원래 숫자를 더하기
    while number>0:
        s += number%10
        number//=10
    number = s + i
    # 생성자가 맞으면 출력하고 루프 빠져나오기 아니면 범위까지 반복
    if number==n:
        print(i)
        answer = True
        break
if not answer:
    print(0)
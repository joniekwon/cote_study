# 각 자리가 숫자 0~9로만 이루어진 문자열 S가 주어졌을 때
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자사이에 x 혹은 +를 넣어
# 결과적으로 만들어 질 수 있는 가장 큰 수를 구하시오

S = '02984'
answer = 0
# 1이하인 숫자는 덧셈이 좋고, 그 외에는 곱셈 수행.
for i in S:
    if answer == 0:
        answer = int(i)
        continue
    if int(i) > 1:
        answer*=int(i)
print(answer)
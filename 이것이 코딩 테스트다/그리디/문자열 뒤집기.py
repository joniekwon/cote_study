# 0과 1로만 이루어진 문자열을 전부 같게 만들기
# 연속으로 붙어있는 같은 숫자는 동시에 뒤집을 수 있음
S = '0001100'
oneToZero = 0
zeroToOne = 0
# 처음 숫자를 통일할 숫자로 뒤집고 카운트
if S[0]=='0':
    zeroToOne+=1
else:
    oneToZero+=1
for i,j in zip(S[:-1], S[1:]):
    if (i =='1' and j=='0'): # 1에서 0으로 바뀌면 0을 1로 뒤집고 카운트
        zeroToOne+=1
    elif (i=='0' and j =='1'): # 0에서 1로 바뀌면 1을 0으로 뒤집고 카운트
        oneToZero+=1
print(min(zeroToOne, oneToZero))

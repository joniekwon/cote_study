# N명의 모험가, 각 모험가는 공포도가 X일 경우 X명 이상으로 구성한 모험가 그룹에 참여해야한다.
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 구해보자

N = 5
X = [2,3,1,2,2]
X.sort()
# 그룹 수, 모험가 수
group, count = 0, 0
for i in X:
    count +=1
    if count<i:
        continue
    else:
        group+=1
        count=0
print(group)
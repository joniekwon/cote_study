import re
from collections import Counter

def solution(str1, str2):
    answer=0
    str1 = str1.lower()
    str2 = str2.lower()
    mulSet1 = Counter()
    mulSet2 = Counter()

    for i in range(0,len(str1)):
        string = ''.join(re.findall('[a-z]', str1[i:i+2]))
        if len(string)==2:
            try:
                mulSet1[string] +=1
            except KeyError:
                mulSet1[string] = 1

    for i in range(0, len(str2)):
        string = ''.join(re.findall('[a-z]', str2[i:i+2]))
        if len(string)==2:
            try:
                mulSet2[string] += 1
            except KeyError:
                mulSet2[string] = 1

    inter = set(mulSet1.keys()) & set(mulSet2.keys())
    union = set(mulSet1.keys()) | set(mulSet2.keys())

    inter_cnt = 0
    for key in inter:
        inter_cnt += min(mulSet1[key], mulSet2[key])

    union_cnt = 0
    for key in union:
        union_cnt += max(mulSet1[key], mulSet2[key])

    if inter_cnt == union_cnt:
        answer = 65536
    else:
        answer= 65536*inter_cnt//union_cnt
    return answer

if __name__ == '__main__':
    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    print(solution(str1,str2))
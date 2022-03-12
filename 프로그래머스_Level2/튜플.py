def solution(s):
    sets = []
    tempStr = ''
    tempList = []
    for i in s[:-1]:
        if i == '{':
            temp = []
        elif i =='}':
            sets.append(tempList)
        if i.isdigit():
            tempStr+=i
        elif i ==",":
            tempList.append(int(tempStr))
            tempStr=''
    sets = sorted(sets, key=lambda x: len(x))
    answer = []
    for l in sets:
        for n in l:
            if n not in answer:
                answer.append(n)
    print(answer)
    return answer

if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    solution(s)
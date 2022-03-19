def solution(list):
    l = sorted(list, key=lambda x: x[1])
    for x in l :
        print(x[0], end=' ')

if __name__=='__main__':
    N = 3
    l = [['홍길동', 95], ['이순신', 77]]
    solution(l)
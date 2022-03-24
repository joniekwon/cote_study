import heapq

def solution(operations):
    max_q = []
    min_q = []
    for i in range(len(operations)):
        operater, number = operations[i].split()
        if operater == 'I':
            heapq.heappush(max_q,-int(number))
            heapq.heappush(min_q,int(number))
        elif len(max_q)<1:
            continue
        elif operater == 'D' and int(number)<0:
            min_value = heapq.heappop(min_q)
            max_q.remove(-min_value)
        elif operater == 'D' and int(number)>0:
            max_value = heapq.heappop(max_q)
            min_q.remove(-max_value)
    try:
        max_value = -heapq.heappop(max_q)
        min_value = heapq.heappop(min_q)
    except:
        max_value = 0
        min_value = 0
    return [max_value, min_value]


if __name__ == '__main__':
    operations =[["I 16","D 1"], ["I 7","I 5","I -5","D -1"]]
    for operation in operations:
        print(solution(operation))

if __name__ == '__main__':
    operations =[["I 16","D 1"], ["I 7","I 5","I -5","D -1"]]
    for operation in operations:
        print(solution(operation))
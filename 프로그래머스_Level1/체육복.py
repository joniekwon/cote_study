# greedy(탐욕법)
def solution(n, lost, reserve):
    student = [1 for x in range(n)]
    for i in lost:
        student[i-1] -=1
    for i in reserve:
        student[i-1] += 1
    i = student.index(0)
    while i < len(student)-1:
        if i>0:
            if student[i-1]>1 and student[i]==0:
                student[i-1],student[i] = 1,1
            elif student[i+1]>1 and student[i]==0:
                student[i + 1], student[i] = 1, 1
        elif student[i+1]>1:
            student[i + 1], student[i] = 1, 1
        i+=1
    #{1: 2, 2: 0, 3: 2, 4: 0, 5: 2}
    idx = 1
    answer=student.count(1)+student.count(2)
    return answer

def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    print(_reserve)
    print(_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

if __name__ == "__main__":
    # N= [5,5,3,3]
    # losts = [[2,4],[2,4],[3],[1,2]]
    # reserves = [[1, 3, 5],[3],[1],[2,3]]
    N=[3]
    losts=[[1,2]]
    reserves=[[2,3]]
    for n, lost, reserve in zip(N,losts,reserves):
        print(solution2(n, lost, reserve))

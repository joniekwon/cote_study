from itertools import permutations
import copy
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    print(dungeons)
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer

if __name__ == '__main__':
    k= 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    print("result: ", solution(k,dungeons))
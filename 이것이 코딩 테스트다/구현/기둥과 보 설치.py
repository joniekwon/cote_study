# 가능한 구조인지 확인하는 함수
def check_possible(answer):
    for x, y, a in answer:
        # 1. a가 기둥0 인경우
        if a==0:
            # 땅에 닿아 있거나, 보의 한쪽 위 또는 기둥 위면 가능
            if y==0 or [x-1, y, 1] in answer or [x,y-1, 0] in answer:
                continue
            else:
                return False
        # 2. a가 보1 인경우
        if a==1:
            # 한쪽 끝부분이 기둥 위, 양쪽이 다른 보와 동시에 연결되어있으면 가능
            if [x, y-1, 0] in answer or [x+1,y-1,0] or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

#
def solution(n, build_frame):
    maps = [[0] for _ in range(n)]
    print(maps)
    answer = [[]]
    for frame in build_frame:
        x, y, isBo, build = frame
        #isBo 0 기둥 1 보 / build 0삭제 1추가
        if build == 1:
            answer.append([x,y,isBo])
            if not check_possible(answer):
                answer.remove([x,y,isBo])
        elif build == 0:
            answer.remove([x,y,isBo])
            if not check_possible(answer):
                answer.append([x,y,isBo])
    return sorted(answer)


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))
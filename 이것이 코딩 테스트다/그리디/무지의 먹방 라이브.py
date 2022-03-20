# 각 음식을 다 먹는데 걸리는 시간(초)가 food_times로 주어짐
# 1초마다 음식을 바꾸어 먹고, 다 먹은 음식은 건너 뛴다.
# 1번 음식부터 먹기 시작한 후 k초 뒤에 먹을 음식의 번호를 구해보자. 먹을 음식이 없으면 -1을 반환
# 아직 미구현
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 길면 먹을 음식이 없으므로 -1 리턴
    if sum(food_times) <= k:
        return -1

    q = []
    # 모든 음식을 우선순위 큐에 넣음
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 총 소요시간
    total = 0
    # 남은 음식 개수
    l = len(food_times)
    # 이전에 먹은 음식 시간
    previous = 0

    # 총 소요시간이 k보다 적고, 음식개수가 하나 이상일 때
    while total<k and l>0:
        # 가장 적게 소요되는 음식부터 큐에서 빼고 걸린 시간을 체크
        now = heapq.heappop(q)[0]


    

if __name__=='__main__':
    print(solution([3,1,2], 5))
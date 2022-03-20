import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 길면 먹을 음식이 없으므로 -1 리턴
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    time = 0; l = len(food_times)

    

if __name__=='__main__':
    print(solution([3,1,2], 5))
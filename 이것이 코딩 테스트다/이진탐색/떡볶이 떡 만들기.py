# 절단기에 높이 H 를 지정하여 떡을 잘라야 한다.
# 떡의 개수 N개와 손님이 요청한 떡의 길이 M이 주어졌을 때 절단기에 설정할수 있는 높이의 최댓값을 구하라
def solution(rice_cakes, target):
    start = 0
    end = max(rice_cakes)

    while (start<=end):
        total = 0
        h = (start + end) // 2
        for x in rice_cakes:
            if x>h:
                total += x-h
        if total<target: # 떡의 길이가 모자라면, h길이를 줄여서 떡을 더 크게 잘라야함
            end = h - 1
        else:
            result = h
            start = h + 1
    return result
if __name__ == '__main__':
    N, M = 4, 6
    rice_cakes = [19, 14, 10, 17]
    print(solution(rice_cakes, M))

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages 가 주어질 때
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
def solution(N, stages):
    s = [0] * (max(stages))
    for x in stages:
        if x<=N:
            s[x] += 1

    users = len(stages)
    fail_rates = []

    for i in range(len(s)):
        fail_rate = s[i]/users
        fail_rates.append((fail_rate, i))
        users -=s[i]

    answer = sorted(fail_rates[1:], key=lambda x: -x[0])
    answer = [x[1] for x in answer]
    return answer

if __name__=="__main__":
    N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
from collections import Counter

def solution(nums):
    # N = 고를 수 있는 폰켓몬 수
    N = len(nums)//2

    answer = Counter(nums)
    return len(answer.most_common(N))

if __name__ == '__main__':
    nums = [3,1,2,3]

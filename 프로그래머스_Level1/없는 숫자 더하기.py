
def solution(numbers):
    answer = sum(range(10))-sum(numbers)
    return answer

if __name__ == "__main__":
    numbers_list = [[1,2,3,4,6,7,8,0],[5,8,4,0,6,7,9]]

    for numbers in numbers_list:
        print(solution(numbers))

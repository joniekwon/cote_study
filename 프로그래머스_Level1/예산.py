def solution(d, budget):
    if sum(d)<budget:
        return len(d)
    else:
        while sum(d)>budget:
            d.pop(d.index(max(d)))
    return len(d)


if __name__ == '__main__':
    d=[1,3,2,5,4]
    budget = 9
    print(solution(d,budget))
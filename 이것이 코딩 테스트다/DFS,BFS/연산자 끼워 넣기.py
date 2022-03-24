from itertools import product


def solution(nums, p):
    s = []
    for i, n in enumerate(p):
        if i==0 and p[i]>0:
            s += ['+'] * n
        elif i==1 and p[i]>0:
            s += ['-'] * n
        elif i==2 and p[i]>0:
            s+= ['*'] * n
        elif i==3 and p[i]>0:
            s+= ['/'] * n

    s = list(product(s, repeat=len(nums)-1))
    min_value = 1e9
    max_value = -1e9
    for i in s:
        temp = 0
        i = ['='] + list(i)
        for number, char in zip(nums,i):
            if temp==0:
                temp = number
                print(number, end=' ')
                continue
            if char == '+':
                temp+=number
            elif char == '-':
                temp-=number
            elif char == '*':
                temp *= number
            elif char == '/':
                temp //= number

        min_value = min(min_value, temp)
        max_value = max(max_value, temp)
    return min_value, max_value


if __name__ == '__main__':
    nums = [[5, 6]]
    P = [[0, 0, 1, 0]]#  덧셈,뺄셈, 곱셈, 나눗셈의 개수,
    for n, p in zip(nums, P):
        m1, m2 = solution(n, p)
        print(m2)
        print(m1)
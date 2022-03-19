def solution(A, B, k):
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(k):
        if A[i]< B[i]:
            A[i], B[i] = B[i], A[i]
    print(sum(A))
if __name__=='__main__':
    A = [1,2,5,4,3]
    B = [5,5,6,6,5]
    k = 3
    solution(A,B, k)
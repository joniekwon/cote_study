# 0 ~ n 까지의 prime numbers 구하기 : 에라토스테네스의 체
def get_prime_nums(n):
    primes = [0, 0] + [1] * (n-1) # 0, 1은 소수가 아님 --> [0,0]
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            primes[2*i::i] = [0]*((n-i)//i)
    return primes

N = int(input())
for i in range(N):
    n = int(input())
    primes = get_prime_nums(n)

    lower, higher = n//2, n//2
    while (primes[lower]!=1) or (primes[higher]!=1):
        lower -=1
        higher +=1
    print(lower, higher)
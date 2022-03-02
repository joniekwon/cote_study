def solution(n, words):
    answer = [0,0]
    q = [0] * len(words)
    for i, w in enumerate(words):
        if i>0 and (fWord!=w[0] or w in q):
            answer[0] = n if (i+1)%n==0 else (i+1)%n
            answer[1] = (i//n)+1
            break
        else:
            fWord = w[-1]
            q[i] = w
    return answer



if __name__ =="__main__":
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
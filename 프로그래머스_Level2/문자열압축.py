import re
from itertools import combinations
import pandas as pd


def solution(s):
    if len(s) <= 2:
        return len(s)

    answer = []
    for i in range(0,len(s)//2+1):
        sub = s[:i]
        compressed = len(sub)
        count = 1
        if len(sub)<1:
            answer.append(len(s))
            continue

        for j in range(i, len(s), i):
            if i+j>len(s):          # 남은 문자열이 압축할 문자보다 짧으면
                compressed += len(s[j:]) # 길이만큼 더하고
                break               # 루프 종료

            if s[j:j+i] != sub:     # 같은 문자열이 아니면
                compressed += len(s[j:j+i]) # 길이만큼 추가하고
                sub = s[j:j+i]      # 압축할 문자열 변경
                if count>1:
                    compressed+=len(str(count))
                count = 1
            else:
                count += 1

        if count>1:
            compressed+=len(str(count))
        answer.append(compressed)

    return min(answer)
import copy

if __name__ == '__main__':
    s="abcabcabcabcdededededede"
    print(solution(s))

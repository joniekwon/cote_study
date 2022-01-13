# participant = ["leo", "kiki", "eden"] #input().split(',')
# completion = ["eden", "kiki"]#input().split(',')
import copy

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
#"leo", "kiki", "eden"
#"eden", "kiki"
def solution(participant, completion):
    dit = {}
    hashValue = 0
    for p in participant:
        dit[hash(p)] = p
        hashValue += hash(p)
    for c in completion:
        hashValue -= hash(c)
    return dit[hashValue]
if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    solution(participant,completion)
    print(solution(participant,completion))
    # 동명이인인데 둘다 완주할 경우도 있음 ㅠㅠ
    # res = list(set(participant)-set(completion))
    # if len(res)>0:
    #     return res[0]
    # else:
    #   names = {}
    #   for name in participant:
    #     if name in names.keys():
    #         return name
    #     else:
    #         names[name]=1

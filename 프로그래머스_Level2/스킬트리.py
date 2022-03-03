def solution(skill, skill_trees):
    answer = len(skill_trees)
    for s in skill_trees:
        i = 1
        for x in s:
            if x in skill and x in skill[:i]:
                i+=1
            elif x in skill and x not in skill[:i]:
                answer-=1
                break
    return answer

if __name__=="__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "BOPQC", "CDOPQB"]

    print(solution(skill, skill_trees))
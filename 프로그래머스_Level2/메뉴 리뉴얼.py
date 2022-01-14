from itertools import combinations

def solution(orders, course):
    menus = {}
    answer = []
    for i in course:
        for j in range(len(orders)):
            comb = map(lambda x:''.join(sorted(x)),list(combinations(orders[j], i)))
            for c in comb:
                try:
                    menus[c]+=1
                except KeyError:
                    menus[c]=1

        keys = [x for x in menus.keys() if len(x) == i]
        vals = [menus[x] for x in menus.keys() if len(x) == i]
        try:
            max_val = max(vals)
            for key in keys:
                if menus[key] == max_val and max_val>1:
                    answer.append(key)
        except:
            answer.extend(keys)
    print(menus)
    return sorted(answer)


if __name__ == '__main__':
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 5]
    print(solution(orders, course))
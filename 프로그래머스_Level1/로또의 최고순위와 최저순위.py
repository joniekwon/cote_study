# lottos=[44, 1, 0, 0, 31, 25]
# win_nums=[31, 10, 45, 1, 6, 19]
lottos=[0,0,0,1,10,45]
win_nums=[31, 10, 45, 1, 6, 19]
win_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
zeroCount = lottos.count(0)
inters = set(lottos).intersection(set(win_nums))
print(inters)
#2--최소 5등
inters_len = len(inters) +zeroCount

print(f"최소 일치 숫자: {len(inters)}")
print(f"최대 일치 숫자: {inters_len}")
print(f"최대 등수: {win_dict[inters_len]},최소 등수: {win_dict[len(inters)]}")
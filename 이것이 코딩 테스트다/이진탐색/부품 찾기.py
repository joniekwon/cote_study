# 가게에는 N개의 부품이 있다. 각 부품에는 정수 형태의 고유한 번호가 있다
# M개 종류의 부품이 모두 있는지 확인하는 프로그램 작성하라.
def solution(Nparts, Mparts):
    for m in Mparts:
        if m in Nparts:
            print("yes", end=' ')
        else:
            print('no', end=' ')

if __name__ == '__main__':
    N, M = 5, 3
    Nparts = [8,3,7,9,2] # 가게에 있는 부품
    Mparts = [5,7,9] # 손님이 찾는 부품
    solution(Nparts,Mparts)
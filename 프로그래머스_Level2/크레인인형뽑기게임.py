
def solution(board,moves):
    answer= 0
    board = list(map(list, zip(*board)))
    q = []
    for i in moves:
        j = 0
        while board[i-1][j]==0 and j<len(board)-1:
            j += 1      # 인형 있는곳까지 들어가기

        if board[i-1][j]!=0:
            try:
                if q[-1]!=board[i - 1][j]: #바구니에 있는 인형 비교해서
                    q.append(board[i - 1][j])   # 다른인형이면 넣고
                elif q[-1]==board[i - 1][j]:
                        q.pop()     # 같은 인형이면 사라짐
                        answer+=1
            except:
                q.append(board[i - 1][j])

            board[i - 1][j] = 0
    return answer*2


if __name__ == '__main__':
    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]

    moves = [1,5,3,5,1,2,1,4]
    print(solution(board,moves))

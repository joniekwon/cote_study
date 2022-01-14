def shift_blocks(board,m):
    board = list(map(list, zip(*board)))
    new_board = []
    for i in board:
        temp = ''.join(i)
        temp = temp.replace(' ', '')
        temp = ' '* (m-len(temp)) + temp
        new_board.append([i for i in temp])
    return list(map(list, zip(*new_board)))

def solution(m,n, board):
    same_block = set()
    board = [list(i) for i in board]
    count = 0
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=' ' and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i+1][j]==board[i+1][j+1]:
                    same_block.add((i,j))
                    same_block.add((i,j+1))
                    same_block.add((i+1,j))
                    same_block.add((i+1,j+1))
        if len(same_block) == 0:
            break
        else:
            count += len(same_block)
            while len(same_block)>=1:
                (i,j) = same_block.pop()
                board[i][j] = ' '
        board = shift_blocks(board,m)

    return count
if __name__ == '__main__':
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m,n,board))
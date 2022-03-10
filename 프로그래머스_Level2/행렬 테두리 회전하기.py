import numpy as np

def solution(rows, columns, queries):
    answer = []
    #board = [[(i+1)+(columns*j) for i in range(columns)] for j in range(rows)]
    board = np.array([x for x in range(1,columns*rows+1)]).reshape(rows,columns)
    for query in queries:
        rotated = []

        y1, x1, y2, x2 = query
        # 움직일 숫자 넣기
        top = board[(y1 - 1), (x1 - 1):x2]
        rotated.extend(top)

        r_top = top[-1]
        board[(y1 - 1), x1:x2] = top[:-1]
        right = board[y1:y2, (x2 - 1)]
        rotated.extend(right)
        r_bottom = right[-1]
        board[y1+1:y2, (x2-1)] = right[:-1]
        board[y1,x2-1] = r_top

        bottom = board[(y2-1), (x1-1):x2]
        rotated.extend(bottom)
        l_bottom = bottom[0]
        board[(y2-1), (x1-1):(x2-1)] = bottom[1:]
        board[(y2-1),(x2-2)] = r_bottom

        left = board[y1:y2, (x1-1)]
        rotated.extend(left)
        board[y1-1:y2-1, (x1-1)] = left
        board[y2-2,(x1-1)] = l_bottom

        answer.append(min(set(rotated)))
    answer = list(map(int,answer))

    return answer


if __name__ == '__main__':
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

    print(solution(rows, columns, queries))


    # for query in queries:
    #     y1, x1, y2, x2 = query
    #     q.extend(board[y1-1,x1-1:x2])
    #     for i in range(y1,y2):
    #         q.append(board[i,x2-1])
    #     q.extend(board[y2-1,x2-2:x1-2:-1])
    #     for i in range(x2-1,x1-1,-1):
    #         q.append(board[i,x1-1])
    #     q.rotate(1)
    #     print(q)

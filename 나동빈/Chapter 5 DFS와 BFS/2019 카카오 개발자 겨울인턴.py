def solution(board, moves):
    moves = [i-1 for i in moves]
    arr = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i] != 0:
                arr.append(board[j][i])
                board[j][i] = 0
                break
    cnt = 0
    res = []
    if len(arr) == 0:
        return 0
    res.append(arr[0])
    print(arr)
    index = 0
    for i in range(1, len(arr)):
        if index < 0:
            res.append(arr[i])
            index = 0
            continue
        if res[index] == arr[i]:
            res.pop()
            index -= 1
            cnt += 1
            continue
        else:
            res.append(arr[i])
            index += 1
    answer = cnt*2

    return answer


board = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 2, 1, 0, 0],

]
board1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [3, 3, 3, 3, 4, 2]
moves1 = [1, 5, 3, 5, 1, 2, 1, 4]


print(solution(board, moves))

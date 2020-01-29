size = int(input('Size--> '))
board = []
win = 0
flag = 0
count = 0
xomark = 0
win_char = 'X'
for i in range(0, size, 1):
    row = []
    for j in range(0, size, 1):
        row.append(flag)
        flag += 1
    board.append(row)


def printboard(board):
    for i in range(0, len(board), 1):
        for j in range(0, len(board) - 1, 1):
            if (str(board[i][j]) in '9a8b7c6d5e4f3g2h1iXj0kO'):
                print(' ' + str(board[i][j]), end=' ')
            else:
                print(board[i][j], end=' ')
        if (str(board[i][-1]) in '9a8b7c6d5e4f3g2h1iXj0kO'):
            print(' ' + str(board[i][-1]))
        else:
            print(board[i][-1])


printboard(board)


def input_board(board, xomark):
    if (xomark == 0):
        x = int(input('X--> '))
        for i in range(0, len(board), 1):
            for j in range(0, len(board), 1):
                if (board[i][j] == x):
                    board[i][j] = 'X'
                    xomark = 1
                    printboard(board)
                    return xomark
    elif (xomark == 1):
        o = int(input('O--> '))
        for i in range(0, len(board), 1):
            for j in range(0, len(board), 1):
                if (board[i][j] == o):
                    board[i][j] = 'O'
                    xomark = 0
                    printboard(board)
                    return xomark


while (win == 0 and count < size ** 2):
    count += 1
    xomark = input_board(board, xomark)

    for i in range(0, len(board), 1):
        flag = 0
        for j in range(1, len(board), 1):
            if (board[i][0] != board[i][j]):
                flag = 1
                break
        if (flag == 0):
            winchar = board[i][0]
            win = 1
            break
    if (win == 0):
        for i in range(0, len(board), 1):
            flag = 0
            for j in range(1, len(board), 1):
                if (board[0][i] != board[j][i]):
                    flag = 1
                    break
            if (flag == 0):
                winchar = board[0][i]
                win = 1
                break
    if (win == 0):
        flag = 0
        for i in range(0, len(board), 1):
            for j in range(0, len(board), 1):
                if (i == j):
                    if (board[i][j] != board[0][0]):
                        flag = 1
                        break
        if (flag == 0):
            winchar = board[0][0]
            win = 1
            break
    if (win == 0):
        flag = 0
        for i in range(0, len(board), 1):
            for j in range(0, len(board), 1):
                if (i + j == size - 1):
                    if (board[i][j] != board[0][size - 1]):
                        flag = 1
                        break
        if (flag == 0):
            winchar = board[0][size - 1]
            win = 1
            break
if (win == 0):
    print('Winner: None')
else:
    print('Winner:', winchar)


















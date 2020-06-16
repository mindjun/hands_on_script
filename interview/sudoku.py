"""
解数独问题
"""


def sudoku():
    board = [['.' for _ in range(9)] for _ in range(9)]
    m, n = 9, 9

    def back_track(i, j):
        if j == n:
            # 从下一行开始
            return back_track(i+1, 0)

        if i == m:
            # 找到一个可行解，触发 base case
            return True

        if board[i][j] != '.':
            back_track(i, j+1)
            return

        for ch in '123456789':
            if not is_valid(i, j, ch):
                continue

            board[i][j] = ch
            if back_track(i, j + 1):
                return True

            board[i][j] = '.'

        # 遍历结束，找不到可行解
        return False

    def is_valid(i, j, ch):
        # todo 判断 3 * 3 的方框空间
        if i >= 1 and j >= 1:
            if board[i-1][j-1] == ch:
                return False

        for index in range(9):
            # 判断行
            if board[i][index] == ch:
                return False
            # 判断列
            if board[index][j] == ch:
                return False

        return True

    back_track(0, 0)
    return board


_board = sudoku()
print(_board)

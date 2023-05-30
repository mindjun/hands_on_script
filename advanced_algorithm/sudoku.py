"""
回溯法
解数独问题
"""


# https://leetcode-cn.com/problems/sudoku-solver/solution/dfshui-su-python-c-java-by-coldme-2/
def sudoku():
    board = [['.' for _ in range(9)] for _ in range(9)]
    m, n = 9, 9

    def back_track(i, j):
        if j == n:
            # 从下一行开始
            return back_track(i + 1, 0)

        if i == m:
            # 找到一个可行解，触发 base case
            return True

        if board[i][j] != '.':
            back_track(i, j + 1)

        for ch in '123456789':
            if not is_valid(i, j, ch):
                continue

            board[i][j] = ch
            if back_track(i, j + 1):
                # 找到一个可行解就推出
                return True
            board[i][j] = '.'

        # 遍历结束，找不到可行解
        return False

    def is_valid(row, col, ch):
        """
        判断是否能在 row， col 这个位置放入 ch 字符
        """
        for i in range(9):
            # 判断行是否存在重复
            if board[row][i] == ch:
                return False
            # 判断列是否存在重复
            if board[i][col] == ch:
                return False
            # 判断 3 x 3 方框是否存在重复
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == ch:
                return False
        return True

    back_track(0, 0)
    return board


_board = sudoku()
print(_board)

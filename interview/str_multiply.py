"""
https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/zi-fu-chuan-cheng-fa
字符串的乘法，不能直接将字符串转换为整数相乘，因为可能越界

    1 2 3
      4 5
__________
      1 5
    1 0
    5
    1 2
    8
  4
___________
  5 5 3 5

可以用一个列表将结果保存起来
保存在 res 列表中的位置为 num1 中字符和 num2 中字符的 index + 1 和 index
"""


def str_multiply(num1, num2):
    res = [0 for _ in range(len(num1) + len(num2))]

    for index1, item1 in enumerate(num1):
        for index2, item2 in enumerate(num2):
            temp_res = int(item1) * int(item2)
            index = index1 + index2
            temp_sum = temp_res + res[index + 1]
            res[index + 1] = temp_sum % 10
            res[index] += temp_sum // 10
    return res


print(str_multiply('123', '45'))

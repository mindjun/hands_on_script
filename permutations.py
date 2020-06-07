# from itertools import permutations, combinations
# items = ['a', 'b', 'c']
#
# for p in permutations(items, 2):
#     print(p)
#
# for c in combinations(items, 3):
#     print(c)
#
#
# def sub_combinations(iter_list, count):
#     result = list()
#     for index, item in enumerate(iter_list):
#         if len(iter_list[index:]) < count:
#             return
#         temp_list = [item]


def sub_combinations_helper(iter_list, count, temp_list):
    if len(iter_list) < count:
        return
    if count == 0:
        result_list.append(temp_list.copy())
        return

    length = len(iter_list)
    for index in range(length - count + 1):
        # 重复使用 temp_list 只是将 temp_list 的部分值给替换掉
        temp_list[-count] = iter_list[index]
        if index + 1 < length:
            sub_combinations_helper(iter_list[index + 1:], count - 1, temp_list)
        else:
            result_list.append(temp_list.copy())


if __name__ == '__main__':
    items = ['a', 'b', 'c', 'd']
    result_list = list()

    old_count = 3
    temp_li = [None for _ in range(old_count)]
    sub_combinations_helper(items, 3, temp_li)
    print(result_list)


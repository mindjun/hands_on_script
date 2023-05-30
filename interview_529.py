import math


def pop_three_count(n):
    nums = list(range(1, n+1))
    k = 0
    while len(nums) > 1:
        index = 0
        while index < len(nums):
            k += 1
            if k % 3 == 0:
                k = 0
                nums.pop(index)
            else:
                index += 1
    return nums


print(pop_three_count(5))
print(pop_three_count(8))


class ListLink(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_next(self, next):
        self.next = next


def count_three(n):
    if n == 1:
        return n
    head = ListLink(1)
    temp_head = head
    for i in range(2, n+1):
        temp = ListLink(i)
        temp_head.set_next(temp)
        temp_head = temp
    temp_head.next = head
    count = 1
    while head.next:
        if count == 2:
            head.next = head.next.next
            count = 1
        else:
            count += 1

        head = head.next
        if head.next.data == head.data:
            break

    return head.data


assert count_three(5) == 4
assert count_three(6) == 1
assert count_three(7) == 4
assert count_three(8) == 7

print(count_three(8))


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(bubble_sort([24, 6, 19, 12, 15, 17, 8, 3, 1, 39]))


def prime_loop_num(n, m):
    result = list()
    cahce = dict()
    for i in range(n, m+1):
        if is_prime(cahce, i) and is_loop(i):
            result.append(i)
    return result


def is_prime(cache, n):
    if n in cache:
        return cache[n]
    for i in range(2, math.ceil(n)):
        if n % i == 0:
            cache[n] = False
            break
    if n not in cache:
        cache[n] = True
    return cache[n]


def is_loop(n):
    return str(n) == str(n)[::-1]


print(prime_loop_num(10, 900))


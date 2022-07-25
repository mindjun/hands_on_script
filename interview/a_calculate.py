"""
a
"""


def calculate(_s):
    def helper(s):
        stack = list()
        num, sign = 0, '+'
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')

            if c == '(':
                num = helper(s)
                print("helper func res: {}".format(num))

            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(0-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                sign = c
                num = 0
            if c == ')':
                break

        return sum(stack)
    return helper(list(_s))


print(calculate('35*(10-4/2)-6'))

# 剑指 offer 第二版，面试题 16
class Power(object):
    @staticmethod
    def power(base, exponent):
        if Power.equal_zero(base) and exponent < 0:
            raise ZeroDivisionError
        res = Power.power_value(base, abs(exponent))
        if exponent < 0:
            return 1.0 / res
        else:
            return res

    @staticmethod
    def equal_zero(num):
        if abs(num - 0.0) < 0.0000001:
            return True
        return False

    @staticmethod
    def power_value(base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        res = Power.power_value(base, exponent >> 1)
        res *= res

        if exponent & 1 == 1:
            res *= base
        return res


# 剑指 offer 第二版，面试题 19
class Match(object):
    def match(self, s, pattern):
        if not s or not pattern:
            return False
        return self.match_helper(s, pattern)

    def match_helper(self, s, pattern):
        if not s and not pattern:
            return True

        if not (s and pattern):
            return False

        # 需要先匹配 * 的情况
        if len(pattern) > 1 and pattern[1] == '*':
            if s[0] == pattern[0] or pattern[0] == '.':
                # s[1:] pattern[2:] 相当于将 * 匹配为 1 个，s[0] 和 pattern[x*] 匹配，移动一位和两位
                # s pattern[2:] 相当于 * 匹配为 0 个
                # s[1:] pattern 相当于 * 匹配为多个，一定 s 一位
                return (self.match_helper(s[1:], pattern[2:]) or self.match_helper(s[1:], pattern)
                        or self.match_helper(s, pattern[2:]))
            else:
                # 如果前一位不想等的情况，只能将 * 匹配为 0 个
                return self.match_helper(s, pattern[2:])

        if s[0] == pattern[0] or pattern[0] == '.':
            return self.match_helper(s[1:], pattern[1:])

        return False


print(Match().match('aaa', 'ab*aa*a'))
print(Match().match('aaaaaa', 'ab*aa*a'))
print(Match().match('aaa', 'aa.a'))
print(Match().match('aaa', 'ab*a'))

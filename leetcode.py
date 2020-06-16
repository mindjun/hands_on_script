class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1 or p[1] != '*':
            if len(s) == 0 or (p[0] != s[0] and p[0] != '.'):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i, length = -1, len(s)
            while i < length and (i < 0 or p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False


s1 = "aaaaaaaaaaaaab"
p1 = "a*a*a*a*a*a*a*a*.*a*c"
print(Solution().isMatch(s1, p1))

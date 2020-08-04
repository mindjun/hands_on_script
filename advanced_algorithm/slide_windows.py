"""
滑动窗口
https://mp.weixin.qq.com/s/ioKXTMZufDECBUwRRp3zaA
https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hua-dong-chuang-kou-ji-qiao-jin-jie
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
"""
from collections import defaultdict
from typing import List


# https://leetcode-cn.com/problems/minimum-window-substring/
# 最小覆盖字串
def min_window(s: str, t: str) -> str:
    need, windows = defaultdict(int), defaultdict(int)
    for c in t:
        need[c] += 1
    left, right = 0, 0
    valid = 0
    start, length = 0, len(s) + 1
    while right < len(s):
        c = s[right]
        right += 1
        # 进行窗口的更新
        if c in need:
            windows[c] += 1
            if windows[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否需要收缩
        while valid == len(need):
            if right - left < length:
                start = left
                length = right - start
            d = s[left]
            left += 1
            # 进行窗口内数据的更新
            if d in need:
                if need[d] == windows[d]:
                    valid -= 1
                windows[d] -= 1
    if length == len(s) + 1:
        return ""
    else:
        return s[start: start + length]


# https://leetcode-cn.com/problems/permutation-in-string/
# 字符串的排列
def check_inclusion(s1: str, s2: str) -> bool:
    window, need = defaultdict(int), defaultdict(int)

    for ch in s1:
        need[ch] += 1

    valid, left, right = 0, 0, 0

    while right < len(s2):
        c = s2[right]
        right += 1

        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 移动left缩小窗口的时机是窗口大小大于t.size()时，因为排列嘛，显然长度应该是一样的
        while right - left >= len(s1):
            if valid == len(need):
                return True
            d = s2[left]
            left += 1

            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return False


# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
# 找到字符串中所有字母异位词
def find_anagrams(s: str, p: str) -> List[int]:
    need, windows = defaultdict(int), defaultdict(int)
    for ch in p:
        need[ch] += 1

    valid, left, right = 0, 0, 0
    result = list()

    while right < len(s):
        c = s[right]
        right += 1

        if c in need:
            windows[c] += 1
            if windows[c] == need[c]:
                valid += 1

        while right - left >= len(p):
            if valid == len(need):
                result.append(left)

            d = s[left]
            left += 1
            if d in need:
                if windows[d] == need[d]:
                    valid -= 1
                windows[d] -= 1
    return result


# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 最长无重复字串
def length_of_longest_substring(s: str) -> int:
    left, right, windows, res = 0, 0, defaultdict(int), 0
    while right < len(s):
        c = s[right]
        right += 1
        windows[c] += 1
        while windows[c] > 1:
            d = s[left]
            windows[d] -= 1
            left += 1
        res = max(res, right - left)
    return res


# 滑动窗口最大值
# https://leetcode-cn.com/problems/sliding-window-maximum/
class MaxSlideQueue(object):
    def __init__(self):
        self.queue = list()

    def push(self, item):
        while self.queue and self.queue[-1] < item:
            self.queue.pop()
        self.queue.append(item)

    def max(self):
        return self.queue[0]

    def pop(self, item):
        # 只有当 item 是最大的值时才删除
        if self.queue[0] == item:
            self.queue = self.queue[1:]


# 滑动窗口最大值
# https://leetcode-cn.com/problems/sliding-window-maximum/
# 该题可与包含 min 方法的栈作比较 https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
def max_slide_windows(list1, size):
    result = list()
    slide_windows = MaxSlideQueue()
    for index, item in enumerate(list1, 1):
        if index < size:
            slide_windows.push(item)
        else:
            slide_windows.push(item)
            result.append(slide_windows.max())
            # pop 的 item 应该是 index - k
            slide_windows.pop(list1[index - size])
    return result


print(f'max_slide_windows ', max_slide_windows(list1=[1, 3, -1, -3, 5, 3, 6, 7], size=3))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0
        elif length == 1:
            return 1

        first = 0
        last = 0
        longest = 0
        current_substring = set()
        while last < length:
            if s[last] in current_substring:
                current_substring.remove(s[first])
                first += 1
            else:
                current_substring.add(s[last])
                longest = max(longest, last - first + 1)
                last += 1
        return longest

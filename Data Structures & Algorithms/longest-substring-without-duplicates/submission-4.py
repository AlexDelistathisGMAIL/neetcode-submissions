class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0
        elif length == 1:
            return 1

        first = 0
        last = 1
        substrings = {}
        current_substring = {s[first]}
        while last < length:
            if s[last] in current_substring:
                substrings[tuple(current_substring)] = last - first
                first += 1
                last = first + 1
                current_substring = {s[first]}
            else:
                current_substring.add(s[last])
                last += 1
    
        if current_substring:
            substrings[tuple(current_substring)] = last - first

        return max(list(substrings.values()))

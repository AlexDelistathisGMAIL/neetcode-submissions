class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(char.lower() for char in s if char.isalnum())
        first = 0
        last = len(t) - 1
        while first != last:
            if t[first] != t[last]:
                return False
            else:
                first += 1
                last -= 1
        return True
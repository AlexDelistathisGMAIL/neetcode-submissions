class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        else:
            a1 = [0] * 26
            a2 = [0] * 26
            first = 0
            last = l1 - 1
            for char in s1:
                a1[ord(char) % 97] += 1
            while last < l2:
                substring = s2[first:last + 1]
                for char in substring:
                    a2[ord(char) % 97] += 1
                if a1 == a2:
                    return True
                else:
                    a2 = [0] * 26
                    first += 1
                    last += 1
            
            return False

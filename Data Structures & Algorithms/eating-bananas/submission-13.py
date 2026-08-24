class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)

        first = 1
        last = maxK
        best = maxK
        while first <= last:
            middle = (first + last) // 2

            bananas = sum((pile + middle - 1) // middle for pile in piles)
            if bananas <= h:
                best = middle
                last = middle - 1
            else:
                first = middle + 1
        
        return best

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)

        first = 1
        last = maxK
        middle = (first + last) // 2
        while middle != 0 and first <= last:
            bananas = sum((pile + middle - 1) // middle for pile in piles)
            print(middle)
            print(bananas)
            if bananas == h:
                return middle
            elif bananas > h:
                first = middle + 1
            else:
                last = middle - 1
            middle = (first + last) // 2
        
        if middle == 0:
            return 1

        bananas = sum((pile + middle - 1) // middle for pile in piles)
        if bananas > h:
            return middle + 1
        else:
            return middle - 1

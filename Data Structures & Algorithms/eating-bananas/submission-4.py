class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        maxK = max(piles)
        sumBananas = sum(piles)
        print(sumBananas)

        if h == length:
            return maxK

        first = 1
        last = maxK
        middle = (first + last) // 2
        while first <= last:
            bananas = middle * h
            print(middle)
            print(bananas)
            if bananas == sumBananas:
                return middle
            elif bananas < sumBananas:
                first = middle + 1
            else:
                last = middle - 1
            middle = (first + last) // 2
        
        bananas = middle * h
        print(middle)
        print(bananas)
        if bananas < sumBananas:
            return middle + 1
        else:
            return middle - 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1

        while first < last:
            middle = (first + last) // 2
            firstElement = nums[first]
            middleElement = nums[middle]
            lastElement = nums[last]
            if middleElement < lastElement:
                last = middle
            else:
                first = middle + 1

        return nums[first]

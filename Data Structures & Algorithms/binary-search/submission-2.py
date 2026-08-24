class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        middle = (first + last) // 2
        while first <= last:
            candidate = nums[middle]
            if candidate == target:
                return middle
            elif candidate < target:
                first = middle + 1
            else:
                last = middle - 1
            middle = (first + last) // 2
            
        return -1

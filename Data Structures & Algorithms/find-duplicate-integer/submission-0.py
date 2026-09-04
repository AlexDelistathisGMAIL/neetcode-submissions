class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        j = i + 1
        while True:
            if nums[i] == nums[j]:
                return nums[i]
            
            if i == length - 1:
                i = 0
            else:
                i += 1
            
            if j == length - 2:
                j = 0
            elif j == length - 1:
                j = 1
            else:
                j += 2

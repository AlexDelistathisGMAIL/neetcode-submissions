class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        length = len(nums)
        for i in range(length):
            element = nums[i]
            if element in mapping:
                return True
            else:
                mapping[element] = 1
        
        return False

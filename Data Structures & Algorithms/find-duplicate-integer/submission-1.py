class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        
        k = 0
        while True:
            i = nums[i]
            k = nums[k]
            if i == k:
                return i

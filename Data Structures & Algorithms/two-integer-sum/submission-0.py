class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        diffs = {}

        for i in range(length):
            diff = target - nums[i]
            print(diff)
            if diff in diffs.keys():
                return [min(i, diffs[diff]), max(i, diffs[diff])]
            else:
                diffs[nums[i]] = i

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first < last:
            middle = (first + last) // 2
            firstElement = nums[first]
            middleElement = nums[middle]
            lastElement = nums[last]
            if middleElement > lastElement:
                first = middle + 1
            else:
                last = middle

        pivot = first
        first, last = 0, len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[last]:
            first = pivot
        else:
            last = pivot - 1

        while first <= last:
            middle = (first + last) // 2
            middleElement = nums[middle]
            if middleElement == target:
                return middle
            elif middleElement < target:
                first = middle + 1
            else:
                last = middle - 1
        return -1

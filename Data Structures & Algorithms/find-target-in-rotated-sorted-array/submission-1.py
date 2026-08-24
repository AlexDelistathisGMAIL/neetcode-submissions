class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first < last:
            middle = (first + last) // 2
            firstElement = nums[first]
            middleElement = nums[middle]
            lastElement = nums[last]
            print(firstElement)
            print(lastElement)
            print(middleElement)
            print("\n")
            if middleElement == target:
                return middle
            elif middleElement < target:
                last = middle
            else:
                first = middle + 1

        return -1

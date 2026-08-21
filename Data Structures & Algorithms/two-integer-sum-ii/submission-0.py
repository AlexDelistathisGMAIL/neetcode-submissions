class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        firstIndex = 0
        secondIndex = 1
        while firstIndex < secondIndex < length:
            firstElement = numbers[firstIndex]
            secondElement = numbers[secondIndex]
            if firstElement + secondElement == target:
                return [firstIndex + 1, secondIndex + 1]
            elif firstElement + secondElement < target:
                if secondIndex == firstIndex + 1:
                    firstIndex += 1
                else:
                    secondIndex += 1

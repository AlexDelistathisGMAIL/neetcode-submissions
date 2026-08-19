class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        firstIndex = 0
        secondIndex = length - 1
        while firstIndex < secondIndex:
            firstElement = numbers[firstIndex]
            secondElement = numbers[secondIndex]
            currentSum = firstElement + secondElement
            if currentSum == target:
                return [firstIndex + 1, secondIndex + 1]
            elif currentSum < target:
                firstIndex += 1
            else:
                secondIndex -= 1

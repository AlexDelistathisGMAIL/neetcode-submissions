class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        firstIndex = 0
        secondIndex = length - 1
        while firstIndex < secondIndex:
            firstHeight = heights[firstIndex]
            secondHeight = heights[secondIndex]
            currentArea = min(firstHeight, secondHeight) * (secondIndex - firstIndex)
            if firstIndex < length - 1 and firstHeight < heights[firstIndex + 1]:
                firstIndex += 1
            elif secondIndex > 0 and secondHeight < heights[secondIndex - 1]:
                secondIndex += 1
            else:
                return currentArea

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        firstIndex = 0
        secondIndex = length - 1
        maxArea = 0
        while firstIndex < secondIndex:
            firstHeight = heights[firstIndex]
            secondHeight = heights[secondIndex]
            smallerHeight = min(firstHeight, secondHeight)
            currentArea = smallerHeight * (secondIndex - firstIndex)
            if currentArea >= maxArea:
                maxArea = currentArea

            if smallerHeight == firstHeight:
                firstIndex += 1
            elif smallerHeight == secondHeight:
                secondIndex -= 1
        
        return maxArea

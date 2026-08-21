class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        sortedPosition, sortedSpeed = zip(*sorted(zip(position, speed)))
        sortedPosition = list(sortedPosition)
        sortedSpeed = list(sortedSpeed)
        fleets = 1
        isFleet = True
        fleetTime = (target - sortedPosition[length - 1]) / sortedSpeed[length - 1]
        i = length - 2
        while i >= 0:
            currentTime = (target - sortedPosition[i]) / sortedSpeed[i]
            if currentTime > fleetTime:
                fleets += 1
                fleetTime = currentTime
                isFleet = False
            i -= 1

        return fleets

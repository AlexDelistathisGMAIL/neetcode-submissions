class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        sortedPosition, sortedSpeed = zip(*sorted(zip(position, speed)))
        sortedPosition = list(sortedPosition)
        sortedSpeed = list(sortedSpeed)
        fleets = []
        currentFleet = [(target - sortedPosition[length - 1]) / sortedSpeed[length - 1], [length - 1]]
        i = length - 2
        while i >= 0:
            currentTime = (target - sortedPosition[i]) / sortedSpeed[i]
            fleetTime = currentFleet[0]
            if currentTime <= fleetTime:
                currentFleet[1].append(i)
                currentFleet[0] = fleetTime
            else:
                fleets.append(currentFleet)
                currentFleet = [currentTime, [i]]
            i -= 1
    
        if currentFleet:
            fleets.append(currentFleet)
            currentFleet = []

        return len(fleets)

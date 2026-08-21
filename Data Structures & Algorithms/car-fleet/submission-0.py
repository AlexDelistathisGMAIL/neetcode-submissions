class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        fleets = []
        currentFleet = [0]
        i = 1
        while i < length:
            if (target - position[i]) / speed[i] <= (target - position[i - 1]) / speed[i - 1]:
                currentFleet.append(i)
            else:
                fleets.append(currentFleet)
                currentFleet = []
            i += 1
        
        if currentFleet:
            fleets.append(currentFleet)
        
        return len(fleets)

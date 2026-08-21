class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sortedNums = sorted(nums)
        triplets = []
        i = 0
        while i < length:
            if sortedNums[i] > 0:
                i += 1
                continue
            j = i + 1
            k = length - 1
            while j < k:
                currentSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if currentSum == 0:
                    triplet = sortedNums[i], sortedNums[j], sortedNums[k]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    j += 1
                elif currentSum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return triplets

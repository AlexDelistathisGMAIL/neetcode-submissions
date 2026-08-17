class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        length = len(nums)

        for i in range(length):
            element = nums[i]
            if element in mapping:
                mapping[nums[i]] += 1
            else:
                mapping[nums[i]] = 1
        
        sorted_mapping = dict(sorted(mapping.items(), key=lambda item: item[1], reverse=True))
        count = 0
        k_most_frequent = []

        for key in sorted_mapping.keys():
            k_most_frequent.append(key)
            count += 1

            if count == k:
                break
        
        return k_most_frequent

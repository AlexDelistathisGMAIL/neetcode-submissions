from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num = len(strs)
        mapping = defaultdict(list)

        for i in range(num):
            element = strs[i]
            length = len(element)
            arr = [0] * 26
            for j in range(length):
                letter = strs[i][j]
                arr[ord(letter) % 97] += 1
            tup = tuple(arr)
            if tup in mapping.keys():
                mapping[tup].append(element)
            else:
                mapping[tup] = [element]
        
        return [mapping[tup] for tup in mapping.keys()]

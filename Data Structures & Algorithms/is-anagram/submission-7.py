class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        sec = {}
        for d in s: 
            if d in first:
                first[d] += 1
            else: 
                first[d] = 0

        for z in t: 
            if z in sec:
                sec[z] += 1
            else: 
                sec[z] = 0    

        return first == sec 
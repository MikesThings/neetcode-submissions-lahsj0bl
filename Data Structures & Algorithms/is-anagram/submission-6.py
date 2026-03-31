class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

# can be made more efficent use len then 1 for loop with len using the index's instead

        for i in s: 
            if (i in map1): 
                map1[i] += 1
            else: 
                map1[i] = 0
        
        for z in t: 
            if (z in map2): 
                map2[z] += 1
            else: 
                map2[z] = 0

        return map1 == map2

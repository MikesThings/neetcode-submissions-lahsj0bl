class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = set()
        maxPath = 1
        # create a numset
        for i in nums:
            numset.add(i)
            
        print(numset)
        for i in numset: 
            path = 1
            while i + 1 in numset:
                path = path + 1
                i = i + 1
            if path > maxPath:
                maxPath = path
        
        return maxPath

            
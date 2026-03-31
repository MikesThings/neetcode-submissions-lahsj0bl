class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       #Error Checking if empty list
        if len(nums) == 0:
            return 0
       #
        numset = set(nums)
        maxPath = 1
        paths = [] 
        for n in numset:
            if (n - 1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                maxPath = max(length, maxPath)
        return maxPath

        return maxPath

            
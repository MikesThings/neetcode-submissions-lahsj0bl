class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solMap = {}
        for i, n in enumerate(nums):
            # solMap[n] = i
            if (n in solMap):
                return [solMap[n], i]
            else:    
                solMap[target - n] = i 

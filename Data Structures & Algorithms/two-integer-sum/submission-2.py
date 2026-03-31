class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {} 
        for i, n in enumerate(nums):
            if (target - n) in mapa:
                return [mapa[target - n], i]
            mapa[n] = i 
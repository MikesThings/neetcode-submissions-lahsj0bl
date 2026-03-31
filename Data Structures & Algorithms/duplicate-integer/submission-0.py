class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        n = len(nums)
        for i in range(n): 
            if nums[i] in dupes: 
                return True
            dupes.add(nums[i])
        return False
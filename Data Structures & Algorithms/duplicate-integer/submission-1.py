class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        n = len(nums)
        for n in nums: 
            if n in dupes: 
                return True
            dupes.add(n)
        return False
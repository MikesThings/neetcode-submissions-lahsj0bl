class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = []
        for n in nums:
            if (n in sol):
                return True
            else: 
                sol.append(n)
        return False
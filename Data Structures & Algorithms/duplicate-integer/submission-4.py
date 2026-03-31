class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doom = set();
        for i in nums: 
            if i in doom: 
                return True;
            else: 
                doom.add(i);
        return False

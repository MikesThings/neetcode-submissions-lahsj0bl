class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            word = set();
            for a in nums: 
                if a in word:
                    return True
                else:
                    word.add(a);
            return False

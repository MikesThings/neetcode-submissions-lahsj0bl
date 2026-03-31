class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i, d  in enumerate(nums): 
            diff = target - d
            if diff in answer: 
                return [answer[diff], i]
            answer[d] = i
        return [0, 0]        
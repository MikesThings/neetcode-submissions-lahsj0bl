class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #params
        size = len(nums)
        output = [1] * size
        
        numPre = 1
        for i in range(size):
            output[i] = numPre 
            numPre *= nums[i]  
        numPost = 1
        for i in range(size - 1, -1 , -1):
            output[i] *= numPost
            numPost *= nums[i]
        return output

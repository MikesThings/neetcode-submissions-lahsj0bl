class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #params
        output = [] 
        length = len(nums) 
        number = 1
        zeroCount = 0
        #nums
        for i in nums:
            if i == 0: 
                zeroCount = zeroCount + 1
            else:
                number = i * number

        # if no 0's
        if zeroCount < 1: 
            for i in range(length):
                output.append(number//nums[i])
        else: 
            if zeroCount == 1:
                for i in range(length): 
                    if nums[i] != 0:
                        output.append(0) 
                    else:
                        output.append(number)

            else: 
                for i in range(length): 
                    output.append(0)
        return output

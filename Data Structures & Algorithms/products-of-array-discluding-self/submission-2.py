class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prod = [1] * n

        # Build prefix product array
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Build suffix product array
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        # Final product = prefix[i] * suffix[i]
        for i in range(n):
            prod[i] = prefix[i] * suffix[i]
        return prod
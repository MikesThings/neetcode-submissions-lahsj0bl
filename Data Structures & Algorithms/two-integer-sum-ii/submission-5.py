class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 1
        R = len(numbers)

        while L < R:
            # Adjust for 1-indexed result
            current_sum = numbers[L - 1] + numbers[R - 1]
            
            if current_sum == target:
                return [L, R]  # Return the 1-indexed positions
            
            elif current_sum > target:
                R -= 1  # Move the right pointer to the left
            
            else:
                L += 1  # Move the left pointer to the right
        
        return []  # Return an empty list if no solution is found

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        k = len(s) - 1
        s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
        
        while i < k:
            start = s[i]
            end = s[k]
            
            # Skip non-alphanumeric characters at the start
            if not start.isalnum():
                i += 1
            # Skip non-alphanumeric characters at the end
            elif not end.isalnum():
                k -= 1
            else:
                # Compare characters
                if start != end:
                    return False
                # Move pointers inward
                i += 1
                k -= 1
        
        return True

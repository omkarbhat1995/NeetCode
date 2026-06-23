class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a given string is a palindrome, considering only
        alphanumeric characters and ignoring case.
        
        Uses an optimal O(1) space two-pointer approach to check characters 
        from the outside in.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer until an alphanumeric character is found
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer until an alphanumeric character is found
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters in lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True
import pytest
from solution import Solution

# Instantiate the solution object once for all tests
sol = Solution()

@pytest.mark.parametrize("s, expected", [
    # Standard Examples
    ("Was it a car or a cat I saw?", True),
    ("tab a cat", False),
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),
    
    # Case Sensitivity Edge Cases
    ("aA", True),
    ("RaceCar", True),
    ("abB", False),
    
    # Non-Alphanumeric & Punctuation Edge Cases
    (" ", True),              # Space only (empty after stripping)
    (".,,," , True),          # Punctuation only
    ("ab@a", True),           # Special character in the middle
    ("a.b,.", False),         # Mixed valid and invalid characters
    
    # Numeric Edge Cases
    ("12321", True),          # Numbers only, palindrome
    ("123a321", True),        # Mixed numbers and letters
    ("0P", False),            # Number and letter, not palindrome
    
    # Boundary Constraints (Length 1)
    ("a", True),              # Single character is always a palindrome
    ("Z", True),              # Single uppercase character
    
    # Extra Edge Cases
    ("race ecar", True),      # Spacing disrupts literal reversal but valid here
])
def test_isPalindrome(s, expected):
    """
    Tests the isPalindrome method against 15+ standard, boundary, and edge cases.
    """
    assert sol.isPalindrome(s) == expected

# Stress test for maximum constraint (length 1000)
def test_isPalindrome_max_constraint():
    """
    Tests a string at the maximum constraint length (1000 characters) 
    to ensure O(n) execution without recursion limits or timeouts.
    """
    large_palindrome = "a" * 500 + "b" * 500
    assert sol.isPalindrome(large_palindrome) == False
    
    large_valid_palindrome = "a" * 1000
    assert sol.isPalindrome(large_valid_palindrome) == True
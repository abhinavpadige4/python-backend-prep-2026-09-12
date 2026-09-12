"""
LeetCode Problem 125: Valid Palindrome
Difficulty: Easy
Focus: Two Pointers

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

Time Complexity: O(n) - We traverse the string once with two pointers
Space Complexity: O(1) - We use only two pointers and constant extra space
"""

def is_palindrome(s: str) -> bool:
    """
    Check if string is a palindrome using two pointers.
    
    Args:
        s: Input string
        
    Returns:
        True if s is palindrome after processing, False otherwise
    """
    # Two pointers approach
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer to previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Alternative approach: Preprocessing + comparison
def is_palindrome_preprocess(s: str) -> bool:
    """
    Check palindrome by preprocessing string first.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - for storing processed string
    """
    # Filter alphanumeric characters and convert to lowercase
    processed = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if processed string is palindrome
    return processed == processed[::-1]

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {is_palindrome(s1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s2 = "race a car"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {is_palindrome(s2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3
    s3 = " "
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {is_palindrome(s3)}")
    print(f"Expected: True")
    print()
    
    # Additional test case
    s4 = "0P"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {is_palindrome(s4)}")
    print(f"Expected: False")
    print()
"""
LeetCode Problem 20: Valid Parentheses
Difficulty: Easy
Focus: Stacks

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

Time Complexity: O(n) - We traverse the string once
Space Complexity: O(n) - In worst case, stack stores all opening brackets
"""

def is_valid(s: str) -> bool:
    """
    Check if parentheses string is valid using stack.
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        True if string is valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map:
            # If stack is empty or top doesn't match, invalid
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
        # Ignore any other characters (though problem says only brackets)
    
    # String is valid if stack is empty (all brackets matched)
    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {is_valid(s1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {is_valid(s2)}")
    print(f"Expected: True")
    print()
    
    # Test case 3
    s3 = "(]"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {is_valid(s3)}")
    print(f"Expected: False")
    print()
    
    # Test case 4
    s4 = "([)]"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {is_valid(s4)}")
    print(f"Expected: False")
    print()
    
    # Test case 5
    s5 = "{[]}"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {is_valid(s5)}")
    print(f"Expected: True")
    print()
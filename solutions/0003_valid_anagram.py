"""
LeetCode Problem 242: Valid Anagram
Difficulty: Easy
Focus: Sorting/Hashing

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Time Complexity: O(n) - We traverse both strings once
Space Complexity: O(1) - The counter stores at most 26 letters (constant)
"""

from typing import Dict

def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s using character counting.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is anagram of s, False otherwise
    """
    # If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Count characters in s
    char_count: Dict[str, int] = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease count for characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    # All counts should be zero
    return all(count == 0 for count in char_count.values())

# Alternative approach using sorting
def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Check anagrams by sorting strings.
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(n) - for storing sorted strings
    """
    return sorted(s) == sorted(t)

# Alternative approach using fixed-size array (for lowercase English letters)
def is_anagram_array(s: str, t: str) -> bool:
    """
    Check anagrams using fixed-size array for better space efficiency.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size 26 array
    """
    if len(s) != len(t):
        return False
    
    # Array to count frequency of each letter (assuming lowercase English)
    count = [0] * 26
    
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    # Check if all counts are zero
    return all(c == 0 for c in count)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Output: {is_anagram(s1, t1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = '{s2}', t = '{t2}'")
    print(f"Output: {is_anagram(s2, t2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3: Empty strings
    s3 = ""
    t3 = ""
    print(f"Input: s = '{s3}', t = '{t3}'")
    print(f"Output: {is_anagram(s3, t3)}")
    print(f"Expected: True")
    print()
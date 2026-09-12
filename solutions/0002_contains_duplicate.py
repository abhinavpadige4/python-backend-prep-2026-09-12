"""
LeetCode Problem 217: Contains Duplicate
Difficulty: Easy
Focus: Sets

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Time Complexity: O(n) - We traverse the list once
Space Complexity: O(n) - We store up to n elements in the set
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains duplicates using a set.
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicates exist, False otherwise
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

# Alternative approaches for comparison

def contains_duplicate_sorting(nums: List[int]) -> bool:
    """
    Check duplicates by sorting first.
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) or O(n) depending on sorting algorithm
    """
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i-1]:
            return True
    return False

def contains_duplicate_brute_force(nums: List[int]) -> bool:
    """
    Brute force approach - check all pairs.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: nums = {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {contains_duplicate(nums3)}")
    print(f"Expected: True")
    print()
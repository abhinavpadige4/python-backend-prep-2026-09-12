"""
LeetCode Problem 1: Two Sum
Difficulty: Easy
Focus: Hash Maps

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Time Complexity: O(n) - We traverse the list once
Space Complexity: O(n) - We store up to n elements in the hash map
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target using hash map.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement we need
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number's index
        num_map[num] = i
    
    # According to problem constraints, this line should never be reached
    return []

# Alternative brute force approach for comparison (O(n^2) time, O(1) space)
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - check all pairs.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    print(f"Expected: [0, 1]")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    print(f"Expected: [1, 2]")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    print(f"Expected: [0, 1]")
    print()
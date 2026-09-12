"""
LeetCode Problem 15: 3Sum
Difficulty: Medium
Focus: Two Pointers/Sorting

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = (-1) + 0 + 1 = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,-1,2] and [-1,0,1].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Time Complexity: O(n^2) - Sorting O(n log n) + two-pointer traversal O(n^2)
Space Complexity: O(1) or O(n) - Depending on sorting algorithm space complexity
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero using two pointers.
    
    Args:
        nums: List of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    # Sort the array first
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach for the remaining array
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1  # Need larger sum
            elif current_sum > 0:
                right -= 1  # Need smaller sum
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {three_sum(nums1)}")
    print(f"Expected: [[-1,-1,2],[-1,0,1]] (order may vary)")
    print()
    
    # Test case 2
    nums2 = [0, 1, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {three_sum(nums2)}")
    print(f"Expected: []")
    print()
    
    # Test case 3
    nums3 = [0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {three_sum(nums3)}")
    print(f"Expected: [[0,0,0]]")
    print()
    
    # Test case 4: Empty array
    nums4 = []
    print(f"Input: nums = {nums4}")
    print(f"Output: {three_sum(nums4)}")
    print(f"Expected: []")
    print()
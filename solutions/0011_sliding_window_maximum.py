"""
LeetCode Problem 239: Sliding Window Maximum
Difficulty: Hard
Focus: Deque/Sliding Window

You are given an array of integers nums, there is a sliding window of size k which 
is moving from the very left of the array to the very right. You can only see the 
k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3 -1 [-3  5  3] 6  7       5
 1  3 -1 -3 [5  3  6] 7       6
 1  3 -1 -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

Time Complexity: O(n) - Each element is pushed and popped from deque at most once
Space Complexity: O(k) - Deque stores at most k elements
"""

from typing import List
from collections import deque

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window of size k using deque.
    
    Args:
        nums: List of integers
        k: Size of sliding window
        
    Returns:
        List containing maximum of each sliding window
    """
    if not nums or k == 0:
        return []
    
    if k == 1:
        return nums
    
    # Deque to store indices of useful elements in current window
    # We maintain decreasing order in deque (front has max element)
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove indices that are out of current window
        while deq and deq[0] <= i - k:
            deq.popleft()
        
        # Remove elements smaller than current from the back
        # They are useless as current element is larger and will stay longer
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        # Add current element's index
        deq.append(i)
        
        # Start adding results once we have first complete window
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

# Alternative approach: Brute force (O(n*k))
def max_sliding_window_brute_force(nums: List[int], k: int) -> List[int]:
    """
    Brute force approach - check each window separately.
    
    Time Complexity: O(n*k)
    Space Complexity: O(n-k+1) for result
    """
    if not nums or k == 0:
        return []
    
    result = []
    n = len(nums)
    
    for i in range(n - k + 1):
        window_max = max(nums[i:i+k])
        result.append(window_max)
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {max_sliding_window(nums1, k1)}")
    print(f"Expected: [3, 3, 5, 5, 6, 7]")
    print()
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {max_sliding_window(nums2, k2)}")
    print(f"Expected: [1]")
    print()
    
    # Test case 3: All same elements
    nums3 = [4, 3, 2, 1, 0]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {max_sliding_window(nums3, k3)}")
    print(f"Expected: [4, 3, 2, 1]")
    print()
    
    # Test case 4: Increasing sequence
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k4 = 3
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {max_sliding_window(nums4, k4)}")
    print(f"Expected: [3, 4, 5, 6, 7, 8, 9, 10]")
    print()
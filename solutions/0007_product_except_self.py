"""
LeetCode Problem 238: Product of Array Except Self
Difficulty: Medium
Focus: Prefix/Suffix Products

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Time Complexity: O(n) - We traverse the array three times
Space Complexity: O(1) - Excluding the output array, we use constant extra space
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Calculate product of array except self using prefix and suffix products.
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is product of all elements except itself
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products (products of all elements to the left)
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Alternative approach using division (not allowed by problem constraints)
def product_except_self_with_division(nums: List[int]) -> List[int]:
    """
    Calculate product using division - NOT allowed by problem constraints.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Count zeros and calculate product of non-zero elements
    zero_count = nums.count(0)
    
    if zero_count > 1:
        # More than one zero means all products are zero
        return [0] * len(nums)
    
    if zero_count == 1:
        # Exactly one zero: only position with zero gets product of others
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        
        result = [0] * len(nums)
        zero_index = nums.index(0)
        result[zero_index] = product
        return result
    
    # No zeros: divide total product by each element
    total_product = 1
    for num in nums:
        total_product *= num
    
    return [total_product // num for num in nums]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {product_except_self(nums1)}")
    print(f"Expected: [24, 12, 8, 6]")
    print()
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {product_except_self(nums2)}")
    print(f"Expected: [0, 0, 9, 0, 0]")
    print()
    
    # Test case 3: Two zeros
    nums3 = [0, 0, 1, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {product_except_self(nums3)}")
    print(f"Expected: [0, 0, 0, 0]")
    print()
    
    # Test case 4: Single zero
    nums4 = [1, 0, 3, 4]
    print(f"Input: nums = {nums4}")
    print(f"Output: {product_except_self(nums4)}")
    print(f"Expected: [0, 12, 0, 0]")
    print()
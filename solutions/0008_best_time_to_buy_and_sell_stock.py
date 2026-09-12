"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Focus: Dynamic Programming

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

Time Complexity: O(n) - We traverse the prices array once
Space Complexity: O(1) - We use only two variables
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculate maximum profit from buying and selling stock once.
    
    Args:
        prices: List of stock prices where prices[i] is price on day i
        
    Returns:
        Maximum profit achievable (0 if no profit possible)
    """
    if len(prices) < 2:
        return 0
    
    # Track minimum price seen so far and maximum profit
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Calculate profit if we sell today (after buying at min_price)
        profit = price - min_price
        
        # Update max_profit if this profit is better
        max_profit = max(max_profit, profit)
        
        # Update min_price if we found a lower price
        min_price = min(min_price, price)
    
    return max_profit

# Alternative approach: Brute force (O(n^2))
def max_profit_brute_force(prices: List[int]) -> int:
    """
    Brute force approach - check all buy/sell pairs.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_profit = 0
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit

# Test cases
if __name__ == "__main__":
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Output: {max_profit(prices1)}")
    print(f"Expected: 5")
    print()
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Output: {max_profit(prices2)}")
    print(f"Expected: 0")
    print()
    
    # Test case 3: Single price
    prices3 = [5]
    print(f"Input: prices = {prices3}")
    print(f"Output: {max_profit(prices3)}")
    print(f"Expected: 0")
    print()
    
    # Test case 4: All same prices
    prices4 = [3, 3, 3, 3]
    print(f"Input: prices = {prices4}")
    print(f"Output: {max_profit(prices4)}")
    print(f"Expected: 0")
    print()
    
    # Test case 5: Increasing prices
    prices5 = [1, 2, 3, 4, 5]
    print(f"Input: prices = {prices5}")
    print(f"Output: {max_profit(prices5)}")
    print(f"Expected: 4")
    print()
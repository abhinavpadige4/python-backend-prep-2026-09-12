"""
LeetCode Problem 155: Min Stack
Difficulty: Medium
Focus: Stack Design

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,-3,null,0,-2,-3]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -3

Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Time Complexity: O(1) for all operations
Space Complexity: O(n) - We store each element along with current minimum
"""

class MinStack:
    """
    MinStack implementation that supports O(1) min retrieval.
    
    Approach: Store each element along with the minimum value seen so far.
    Each stack element is a tuple (value, current_min).
    """
    
    def __init__(self):
        """Initialize empty stack."""
        self.stack = []  # List of tuples (value, current_min)
    
    def push(self, val: int) -> None:
        """
        Push element onto stack.
        
        Args:
            val: Value to push onto stack
        """
        if not self.stack:
            # If stack is empty, current value is the minimum
            current_min = val
        else:
            # Otherwise, minimum is min of current value and previous minimum
            current_min = min(val, self.stack[-1][1])
        
        self.stack.append((val, current_min))
    
    def pop(self) -> None:
        """
        Remove the element on top of the stack.
        """
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        """
        Get the top element of the stack.
        
        Returns:
            Top element value
        """
        if self.stack:
            return self.stack[-1][0]
        raise IndexError("Stack is empty")
    
    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        
        Returns:
            Minimum element value
        """
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("Stack is empty")

# Alternative approach: Two stacks (one for values, one for minimums)
class MinStackTwoStacks:
    """
    MinStack using two separate stacks:
    - main stack for all values
    - min stack for tracking minimums
    """
    
    def __init__(self):
        self.stack = []      # Main stack for values
        self.min_stack = []  # Stack for tracking minimums
    
    def push(self, val: int) -> None:
        """Push value onto both stacks appropriately."""
        self.stack.append(val)
        
        # Push to min_stack if it's empty or val is <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        """Pop from both stacks if needed."""
        if self.stack:
            val = self.stack.pop()
            # If popped value equals current minimum, pop from min_stack too
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        """Get top value from main stack."""
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")
    
    def getMin(self) -> int:
        """Get current minimum from min_stack."""
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")

# Test cases
if __name__ == "__main__":
    # Test case from problem description
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"getMin(): {min_stack.getMin()}")  # returns -3
    min_stack.pop()
    print(f"top(): {min_stack.top()}")        # returns 0
    print(f"getMin(): {min_stack.getMin()}")  # returns -3
    print()
    
    # Additional test cases
    min_stack2 = MinStack()
    min_stack2.push(0)
    min_stack2.push(1)
    min_stack2.push(0)
    print(f"getMin(): {min_stack2.getMin()}")  # returns 0
    min_stack2.pop()
    print(f"getMin(): {min_stack2.getMin()}")  # returns 0
    print()
    
    # Test with negative numbers
    min_stack3 = MinStack()
    min_stack3.push(-3)
    min_stack3.push(0)
    min_stack3.push(-5)
    print(f"getMin(): {min_stack3.getMin()}")  # returns -5
    min_stack3.pop()
    print(f"getMin(): {min_stack3.getMin()}")  # returns -3
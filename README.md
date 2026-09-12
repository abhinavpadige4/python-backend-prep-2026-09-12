# Python Backend Interview Preparation - 3 Day Plan

This repository contains solutions to 12 LeetCode problems designed for Python backend interview preparation, following a 3-day study plan.

## 📋 Overview

- **Total Problems**: 12 LeetCode problems
- **Duration**: 3 days
- **Focus**: Python fundamentals, data structures, algorithms, and backend concepts
- **Difficulty Mix**: 5 Easy, 5 Medium, 2 Hard

## 📅 3-Day Study Plan

### Day 1: Python Fundamentals & Data Structures
**Focus**: Lists, Dicts, Sets, Tuples, Generators, Iterators, Decorators, Context Managers, OOP, Time/Space Complexity
**Problems**:
1. [Two Sum](#1-two-sum-leetcode-1) - Hash Maps
2. [Contains Duplicate](#2-contains-duplicate-leetcode-217) - Sets
3. [Valid Anagram](#3-valid-anagram-leetcode-242) - Sorting/Hashing
4. [Valid Palindrome](#4-valid-palindrome-leetcode-125) - Two Pointers

### Day 2: Algorithms & Backend Core
**Focus**: Recursion, Trees, Graphs, BFS/DFS, REST API Design, SQL vs NoSQL, Caching Strategies
**Problems**:
5. [Valid Parentheses](#5-valid-parentheses-leetcode-20) - Stacks
6. [3Sum](#6-3sum-leetcode-15) - Two Pointers/Sorting
7. [Product of Array Except Self](#7-product-of-array-except-self-leetcode-238) - Prefix/Suffix Products
8. [Best Time to Buy and Sell Stock](#8-best-time-to-buy-and-sell-stock-leetcode-121) - Dynamic Programming

### Day 3: Concurrency, System Design & Mock Interview
**Focus**: Threading vs Multiprocessing vs Asyncio, GIL, Race Conditions, Docker, CI/CD, System Design
**Problems**:
9. [LRU Cache](#9-lru-cache-leetcode-146) - Hash Map + Doubly Linked List
10. [Implement Trie](#10-implement-trie-leetcode-208) - Trees/Prefixes
11. [Sliding Window Maximum](#11-sliding-window-maximum-leetcode-239) - Deque/Sliding Window
12. [Min Stack](#12-min-stack-leetcode-155) - Stack Design

## 🔧 Solutions

### 1. Two Sum (LeetCode #1)
- **File**: `solutions/0001_two_sum.py`
- **Approach**: Hash Map (dictionary) for O(n) lookup
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Key Concept**: Using hash map to store complement values

### 2. Contains Duplicate (LeetCode #217)
- **File**: `solutions/0002_contains_duplicate.py`
- **Approach**: Set for O(1) average lookup time
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Key Concept**: Early termination when duplicate found

### 3. Valid Anagram (LeetCode #242)
- **File**: `solutions/0003_valid_anagram.py`
- **Approach**: Character counting with hash map
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - fixed alphabet size
- **Key Concept**: Frequency counting comparison

### 4. Valid Palindrome (LeetCode #125)
- **File**: `solutions/0004_valid_palindrome.py`
- **Approach**: Two pointers with alphanumeric filtering
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: In-place comparison without extra space

### 5. Valid Parentheses (LeetCode #20)
- **File**: `solutions/0005_valid_parentheses.py`
- **Approach**: Stack for matching pairs
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Key Concept**: LIFO property for bracket matching

### 6. 3Sum (LeetCode #15)
- **File**: `solutions/0006_3sum.py`
- **Approach**: Sorting + Two pointers
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1) or O(n) depending on sort
- **Key Concept**: Duplicate skipping and two-pointer technique

### 7. Product of Array Except Self (LeetCode #238)
- **File**: `solutions/0007_product_except_self.py`
- **Approach**: Prefix and suffix products
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) excluding output
- **Key Concept**: Division-free solution using prefix/suffix

### 8. Best Time to Buy and Sell Stock (LeetCode #121)
- **File**: `solutions/0008_best_time_to_buy_and_sell_stock.py`
- **Approach**: Single pass tracking min price and max profit
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Concept**: Dynamic programming state tracking

### 9. LRU Cache (LeetCode #146)
- **File**: `solutions/0009_lru_cache.py`
- **Approach**: Hash map + Doubly linked list
- **Time Complexity**: O(1) for get/put
- **Space Complexity**: O(capacity)
- **Key Concept**: Combining O(1) access with ordering

### 10. Implement Trie (LeetCode #208)
- **File**: `solutions/0010_implement_trie.py`
- **Approach**: Prefix tree with node children mapping
- **Time Complexity**: O(L) per operation (L = word length)
- **Space Complexity**: O(N×L) where N = word count
- **Key Concept**: Efficient prefix-based storage and retrieval

### 11. Sliding Window Maximum (LeetCode #239)
- **File**: `solutions/0011_sliding_window_maximum.py`
- **Approach**: Monotonic deque for maximum tracking
- **Time Complexity**: O(n)
- **Space Complexity**: O(k)
- **Key Concept**: Maintaining decreasing order in deque

### 12. Min Stack (LeetCode #155)
- **File**: `solutions/0012_min_stack.py`
- **Approach**: Stack storing (value, current_min) tuples
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n)
- **Key Concept**: Tracking minimum with each element

## 🚀 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhinavpadige4/python-backend-prep-2026-09-12.git
   ```

2. **Run individual solutions**:
   ```bash
   python solutions/0001_two_sum.py
   ```

3. **Study the approaches**:
   - Each solution includes detailed comments
   - Time/space complexity analysis
   - Alternative approaches where relevant
   - Test cases demonstrating usage

## 📚 Key Concepts Covered

### Data Structures
- Arrays/Lists
- Hash Maps/Dictionaries
- Sets
- Stacks
- Queues/Deques
- Trees (Trie)
- Linked Lists (Doubly Linked List)

### Algorithms
- Two Pointers Technique
- Sliding Window
- Prefix Sum/Product
- Sorting-based approaches
- Greedy algorithms
- Dynamic Programming concepts

### System Design Concepts
- LRU Cache implementation
- Trie for autocomplete systems
- Stack extensions for additional functionality
- Efficient data retrieval patterns

### Python-Specific Features
- Type hints for better code documentation
- List comprehensions
- Collections.deque for efficient queue operations
- Object-oriented design patterns

## ✅ Validation Criteria

All solutions meet the following criteria:
- ✅ Correctly solve the given problem
- ✅ Optimal time and space complexity
- ✅ Clean, readable code with comments
- ✅ Include test cases for verification
- ✅ Handle edge cases appropriately
- ✅ Follow Python best practices and PEP 8 guidelines

## 🔗 Resources

- [Python Interview Preparation Guide](https://hackajob.com/en-us/talent/technical-assessment/python-interview-preparation-guide)
- [Python Interview Questions Repo](https://github.com/Devinterview-io/python-interview-questions)
- [NeetCode 250 Guide](https://github.com/ascherj/neetcode-250-guide)
- [LeetCode Python Problem Set](https://leetcode.com/problemset?language=Python)

---

*Prepared for Python backend interview preparation - September 2026*
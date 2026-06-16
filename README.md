# 🚀 LeetCode Solutions Repository

Welcome to my LeetCode Solutions Repository! This repository contains my solutions to LeetCode problems along with detailed explanations, approaches, complexity analysis, and clean Python implementations.

The goal of this repository is to document my problem-solving journey, strengthen my Data Structures & Algorithms skills, and prepare for coding interviews.

---

## 📌 About

This repository includes:

- ✅ LeetCode problem solutions
- ✅ Intuition behind each solution
- ✅ Step-by-step approach
- ✅ Time & Space Complexity Analysis
- ✅ Clean and readable Python code
- ✅ Multiple approaches when applicable
- ✅ Categorization by topic

---

## 🛠️ Topics Covered

### Arrays
- Two Pointers
- Prefix Sum
- Sliding Window
- Matrix Operations
- Sorting

### Strings
- String Manipulation
- Pattern Matching
- Hashing
- String Simulation

### Linked Lists
- Singly Linked List
- Doubly Linked List
- Fast & Slow Pointer

### Stacks & Queues
- Monotonic Stack
- Queue Simulation
- Expression Evaluation

### Trees
- Binary Tree
- Binary Search Tree
- Tree Traversals
- Lowest Common Ancestor

### Graphs
- BFS
- DFS
- Topological Sorting
- Shortest Path Algorithms
- Union Find

### Dynamic Programming
- Linear DP
- Knapsack DP
- Interval DP
- Prefix DP

### Greedy Algorithms
- Interval Scheduling
- Heap-Based Greedy
- Sorting-Based Greedy

### Backtracking
- Subsets
- Permutations
- Combinations
- N-Queens

### Bit Manipulation
- XOR Tricks
- Bitmasking
- Set Bit Operations

### Binary Search
- Search Space Reduction
- Lower Bound / Upper Bound
- Binary Search on Answer

### Heaps & Priority Queues

### Tries

### Segment Trees

### Advanced Algorithms

---

## 📂 Solution Format

Each solution follows a consistent format:

```markdown
# Intuition

# Approach

# Complexity
- Time Complexity:
- Space Complexity:

# Code
```

Example:

```python
class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
```

---

## 🎯 Goals

- Solve 500+ LeetCode problems
- Master Data Structures & Algorithms
- Improve problem-solving skills
- Prepare for coding interviews
- Build strong competitive programming foundations

---

## 📈 Progress

| Difficulty | Solved  |
|------------|---------|
| Easy       | 🚧     |   
| Medium     | 🚧     |
| Hard       | 🚧     |
| Total      | 🚧     |

---

## 🏆 Problem Solving Philosophy

1. Understand the problem completely.
2. Start with a brute-force solution.
3. Identify patterns and optimizations.
4. Derive the optimal approach.
5. Analyze complexity.
6. Write clean and maintainable code.

---

## 💻 Language Used

- Python 🐍

Future additions may include:
- Java
- C++
- JavaScript

---

## 🌟 Why This Repository?

This repository serves as:

- A personal DSA notebook
- Interview preparation material
- A collection of coding patterns
- A reference for future problem solving

---

## 📬 Connect With Me

**Giripriyan S**

- GitHub: https://github.com/giripriyansenthilkumar
- LinkedIn: https://www.linkedin.com/in/giripriyan-s
- Leetcode: https://leetcode.com/u/giripriyansenthilkumar/

---

### ⭐ If you find this repository helpful, consider giving it a star!

"Consistency is the key to mastering algorithms."
# Intuition
To maximize the size of the array after performing the allowed operations, we want to keep as many elements as possible while maintaining a non-decreasing sequence. As we traverse the array, we keep track of the last accepted element. If the current element is greater than or equal to the previously accepted element, it can be included in the final array; otherwise, it is skipped.

# Approach
1. Initialize a counter `c` to store the size of the resulting array.
2. Maintain a variable `prev` representing the last accepted value.
3. Traverse the array from left to right:
   - If the current element is greater than or equal to `prev`, include it in the result.
   - Update `prev` to the current element and increment the counter.
4. Return the counter as the maximum possible size.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

# Code
```python
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        c = 0
        prev = -1

        for num in nums:
            if num >= prev:
                prev = num
                c += 1

        return c
```
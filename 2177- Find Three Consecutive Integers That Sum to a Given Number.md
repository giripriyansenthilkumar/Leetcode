# Intuition
Let the three consecutive integers be `x - 1`, `x`, and `x + 1`.

Their sum is:

`(x - 1) + x + (x + 1) = 3x`

This means the given number must be divisible by `3`. If it is, the middle number is `num // 3`, and the required three integers can be constructed directly.

# Approach
1. Check if `num` is divisible by `3`.
2. If not, no three consecutive integers can sum to `num`, so return an empty list.
3. Otherwise:
   - Compute the middle integer as `num // 3`.
   - Return `[middle - 1, middle, middle + 1]`.

# Complexity
- Time complexity: **O(1)**
  - Only a few arithmetic operations are performed.

- Space complexity: **O(1)**
  - Uses a constant amount of extra space.

# Code
```python []
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            middle = num // 3
            return [middle - 1, middle, middle + 1]

        return []
```
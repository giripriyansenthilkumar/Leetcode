# Intuition
Each student consumes a fixed amount of chalk in a cyclic manner. Instead of repeatedly simulating the entire process until the chalk runs out, we can observe that one complete round consumes `sum(chalk)` chalk pieces.

By taking `k % sum(chalk)`, we determine the amount of chalk remaining after removing all complete cycles. We then simulate only the final partial cycle to find the student who cannot be served.

# Approach
1. Compute the total chalk required for one complete round.
2. Reduce `k` using modulo:
   - `remaining = k % total_chalk`
3. Traverse the `chalk` array:
   - Subtract each student's chalk requirement from `remaining`.
   - If `remaining` becomes negative, that student cannot receive enough chalk and is the answer.
4. Return the corresponding index.

# Complexity
- Time complexity: **O(n)**
  - One pass to compute the sum and one pass to find the answer.

- Space complexity: **O(1)**
  - Only a few extra variables are used.

# Code
```python
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        remaining = k % total_chalk

        for student_index in range(len(chalk)):
            remaining -= chalk[student_index]

            if remaining < 0:
                return student_index

        return -1
```
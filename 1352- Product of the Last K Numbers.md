# Intuition
To find the product of the last `k` numbers, we can directly extract the last `k` elements from the list and compute their product.

Since all numbers are stored in insertion order, the last `k` numbers always form a contiguous subarray at the end of the list. Using Python's built-in `math.prod()` function allows us to efficiently calculate the product of these elements.

# Approach
1. Maintain a list to store all added numbers.
2. When `add(num)` is called, append the number to the list.
3. When `getProduct(k)` is called:
   - Extract the last `k` elements using slicing.
   - Compute and return their product using `math.prod()`.

# Complexity
- Time complexity:
  - `add(num)`: **O(1)**
  - `getProduct(k)`: **O(k)**, since we multiply the last `k` elements.

- Space complexity:
  - **O(n)**, where `n` is the total number of inserted numbers.

# Code
```python []
import math

class ProductOfNumbers:

    def __init__(self):
        self.numbers = []
        self.size = 0

    def add(self, num: int) -> None:
        self.numbers.append(num)
        self.size += 1

    def getProduct(self, k: int) -> int:
        return math.prod(self.numbers[self.size - k:])
# Intuition
We need to support two operations:

- `popSmallest()` → Remove and return the smallest available number.
- `addBack(num)` → Add a previously removed number back into the set if it is not already present.

A simple way to achieve this is to maintain a list of available numbers. For `popSmallest()`, we find the minimum element, remove it, and return it. For `addBack(num)`, we insert the number back only if it is not already in the list.

# Approach
1. Initialize the set with numbers from `1` to `1000`.
2. For `popSmallest()`:
   - Find the smallest element using `min()`.
   - Locate its index and remove it from the list.
   - Return the removed value.
3. For `addBack(num)`:
   - Check whether `num` already exists in the list.
   - If not, append it back.

# Complexity
- Time complexity:
  - `popSmallest()`: **O(n)**
    - Finding the minimum and locating its index both take linear time.
  - `addBack()`: **O(n)**
    - Membership check in a list takes linear time.

- Space complexity:
  - **O(n)**
    - Stores all available numbers in the list.

# Code
```python
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]

    def popSmallest(self) -> int:
        smallest = min(self.nums)
        index = self.nums.index(smallest)
        return self.nums.pop(index)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```
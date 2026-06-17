# Intuition
A number is valid if there exists some integer `x` such that:

x + reverse(x) = num

So, we can either check every possible number one by one, or precompute all possible values of `x + reverse(x)` and directly check whether `num` exists in that set.

# Approach 1: Brute Force
For every number from `0` to `num - 1`, reverse it and check whether:


```i + reverse(i) = num```


If any value satisfies the condition, return `True`. Otherwise, return `False`.

# Complexity
- Time complexity:
$$O(n \log n)$$

- Space complexity:
$$O(1)$$

# Code
```python
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True

        for i in range(num):
            if i + int(str(i)[::-1]) == num:
                return True

        return False
```

---

# Approach 2: Precomputation
Instead of checking every number for each test case, we can precompute all possible values of:

```i + reverse(i)```

for numbers from `0` to `100000`.

Then, for every input `num`, we only need to check whether it exists in the set.

# Complexity
- Time complexity:
$$O(1)$$

- Space complexity:
$$O(100000)$$

# Code
```python
class Solution:
    valid = set()

    for i in range(100001):
        valid.add(i + int(str(i)[::-1]))

    def sumOfNumberAndReverse(self, num: int) -> bool:
        return num in self.valid
```
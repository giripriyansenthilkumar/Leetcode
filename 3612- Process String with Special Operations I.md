# Intuition
We process the string from left to right and maintain the current result. For each character, we perform the corresponding operation on the result string:
- `*` removes the last character.
- `#` duplicates the current string.
- `%` reverses the current string.
- Any other character is appended to the result.

By simulating these operations in order, we obtain the final processed string.

# Approach
1. Initialize an empty string `res`.
2. Iterate through each character in the input string.
3. Apply the required operation based on the character:
   - Remove the last character for `*`.
   - Duplicate the current string for `#`.
   - Reverse the current string for `%`.
   - Append normal characters to the result.
4. Return the final value of `res`.

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n)$$

# Code
```python
class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for x in s:
            if x == '*':
                res = res[:-1]
            elif x == '#':
                res += res
            elif x == '%':
                res = res[::-1]
            else:
                res += x

        return res
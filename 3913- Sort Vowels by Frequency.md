# Intuition
To sort the vowels in the string while keeping all non-vowel characters in their original positions, we first collect all vowels and count their occurrences. Then, we construct a list of vowels based on their frequencies and place them back into the string at vowel positions. This allows us to modify only the vowels while preserving the structure of the original string.

# Approach
1. Convert the string into a list so characters can be modified in place.
2. Traverse the string and count the frequency of each vowel using a dictionary.
3. Build a list containing all vowels according to their frequencies.
4. Sort the collected vowels.
5. Traverse the character list again:
   - Whenever a vowel position is encountered, replace it with the next vowel from the sorted list.
6. Join the list back into a string and return the result.

# Complexity
- Time complexity:
$$O(n + k \log k)$$

where:
- \(n\) is the length of the string.
- \(k\) is the number of vowels.

- Space complexity:
$$O(k)$$

for storing the vowels and their frequencies.

# Code
```python
class Solution:
    def sortVowels(self, s: str) -> str:
        lst = list(s)
        f = {}
        v = ['a', 'e', 'i', 'o', 'u']

        for i in s:
            if i in v:
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 1

        ans = []
        for x in f:
            for i in range(f[x]):
                ans.append(x)

        ans = sorted(ans, key=lambda x: (-f[x]))

        j = 0
        for i in range(len(lst)):
            if j == len(ans):
                break

            if lst[i] in v:
                lst[i] = ans[j]
                j += 1

        return "".join(lst)
```
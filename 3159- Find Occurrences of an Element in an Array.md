# Intuition
To answer each query efficiently, we first record the indices where the target value `x` appears in the array.

The first occurrence corresponds to the first stored index, the second occurrence to the second stored index, and so on. For each query `q`, we simply return the index of the `q`-th occurrence if it exists; otherwise, return `-1`.

# Approach
1. Traverse `nums` and keep track of every occurrence of `x`.
2. Store the occurrence number as the key and its index as the value in a dictionary.
3. Let `count` be the total number of occurrences of `x`.
4. For each query:
   - If `q > count`, append `-1` to the answer.
   - Otherwise, append the index corresponding to the `q`-th occurrence.
5. Return the resulting list.

# Complexity
- Time complexity: **O(n + m)**
  - `n` = length of `nums`
  - `m` = length of `queries`
  - One pass to record occurrences and one pass to answer queries.

- Space complexity: **O(k)**
  - `k` = number of occurrences of `x`
  - Used to store occurrence indices.

# Code
```python
class Solution:
    def occurrencesOfElement(
        self,
        nums: List[int],
        queries: List[int],
        x: int
    ) -> List[int]:

        occurrence_indices = {}
        occurrence_count = 0

        for index in range(len(nums)):
            if nums[index] == x:
                occurrence_count += 1
                occurrence_indices[occurrence_count] = index

        answer = []

        for query in queries:
            if query > occurrence_count:
                answer.append(-1)
            else:
                answer.append(occurrence_indices[query])

        return answer
```
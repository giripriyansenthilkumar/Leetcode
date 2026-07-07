# Intuition
We need to find numbers that appear at least three times consecutively in the `Logs` table.

By comparing three consecutive rows, we can identify such numbers. If three rows have consecutive `id` values and the same `num`, then that number satisfies the condition. Since the same number may appear in multiple overlapping sequences, we use `DISTINCT` to avoid duplicates.

# Approach
1. Treat the `Logs` table as three separate aliases (`t1`, `t2`, and `t3`).
2. Ensure that:
   - `t1.id = t2.id + 1`
   - `t2.id = t3.id + 1`
   - All three rows have the same `num`.
3. Select the number using `DISTINCT` to remove duplicate results.

# Complexity
- **Time complexity:** **O(n²)**
  - The self-join compares rows from the same table. Depending on the database optimizer and indexing, the effective performance may vary.

- **Space complexity:** **O(1)**
  - Only a constant amount of extra space is used.

# Code

### MySQL
```sql
SELECT DISTINCT
    t1.num AS ConsecutiveNums
FROM Logs t1,
     Logs t2,
     Logs t3
WHERE t1.id = t2.id + 1
  AND t2.id = t3.id + 1
  AND t1.num = t2.num
  AND t2.num = t3.num;
```
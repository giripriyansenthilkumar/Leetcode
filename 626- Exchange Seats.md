# Intuition
We need to swap the seat IDs of every pair of adjacent students.

- If a student's ID is odd and the next ID exists, swap it with the next seat.
- If a student's ID is even, swap it with the previous seat.
- If the last student has no partner (i.e., an odd ID with no next ID), keep the same ID.

A `CASE` expression allows us to determine the new seat ID for each student.

# Approach
1. For each row:
   - If the ID is odd and the next ID exists, assign `id + 1`.
   - If the ID is even, assign `id - 1`.
   - Otherwise, keep the original ID.
2. Return the modified IDs along with the student names.
3. Sort the result by the new seat ID.

# Complexity
- **Time complexity:** **O(n)**
  - Each row is processed once.

- **Space complexity:** **O(1)**
  - Only a constant amount of extra space is used.

# Code

### MySQL
```sql
SELECT
    CASE
        WHEN id % 2 = 1
             AND id + 1 IN (SELECT id FROM Seat)
        THEN id + 1

        WHEN id % 2 = 0
        THEN id - 1

        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;
```
# Intuition
People board the bus in the order of their turn. We keep a running total of the passengers' weights as they board.

The last person who can board is the one whose cumulative weight does not exceed the bus capacity of **1000**. A window function is used to efficiently compute the cumulative weight for each person.

# Approach
1. Use a window function to calculate the cumulative sum of `weight` ordered by `turn`.
2. Store the cumulative weight for every person.
3. Filter the rows where the cumulative weight is less than or equal to `1000`.
4. Sort these remaining rows by cumulative weight in descending order.
5. Return the first person's name.

# Complexity
- **Time complexity:** **O(n log n)**
  - Sorting by `turn` for the window function dominates the computation.

- **Space complexity:** **O(n)**
  - The derived table stores the cumulative weight for each row.

# Code

### MySQL
```sql
SELECT person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) AS t
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
```
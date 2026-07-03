# Intuition
For each product, we need to retrieve the record corresponding to its first year of sale.

We first determine the minimum year for every `product_id` using aggregation. Then, we select the rows from the `Sales` table whose `(product_id, year)` pair matches the earliest year for that product.

# Approach
1. Group the `Sales` table by `product_id`.
2. Find the minimum `year` for each product.
3. Match these `(product_id, year)` pairs with the original table.
4. Return the required columns:
   - `product_id`
   - `first_year`
   - `quantity`
   - `price`

# Complexity
- **Time complexity:** **O(n)**
  - One scan to compute the minimum year for each product and another to filter the matching rows.

- **Space complexity:** **O(n)**
  - The grouped result stores one entry for each distinct product.

# Code

### MySQL
```sql
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT
        product_id,
        MIN(year)
    FROM Sales
    GROUP BY product_id
);
```
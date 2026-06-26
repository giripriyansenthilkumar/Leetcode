# Intuition
Each operation replaces one value in the array with another.

Searching for the old value every time would be inefficient. Instead, we maintain a hash map that stores the current index of every value in the array. This allows each replacement to be performed in constant time by directly accessing the index of the value to be replaced.

# Approach
1. Create a hash map that maps each array value to its current index.
2. For every operation `[old, new]`:
   - Find the index of `old` using the hash map.
   - Replace `old` with `new` in the array.
   - Update the hash map so that `new` points to the same index.
3. After processing all operations, return the modified array.

# Complexity
- Time complexity: **O(n + m)**
  - `n` = length of `nums`
  - `m` = number of operations
  - Building the hash map takes `O(n)` and each operation takes `O(1)`.

- Space complexity: **O(n)**
  - The hash map stores the index of each element.

# Code

### Python
```python
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        position = {}

        for index, value in enumerate(nums):
            position[value] = index

        for old, new in operations:
            nums[position[old]] = new
            position[new] = position[old]
            del position[old]

        return nums
```

### Java
```java
class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        HashMap<Integer, Integer> position = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            position.put(nums[i], i);
        }

        for (int[] operation : operations) {
            int oldValue = operation[0];
            int newValue = operation[1];

            int index = position.get(oldValue);

            nums[index] = newValue;

            position.remove(oldValue);
            position.put(newValue, index);
        }

        return nums;
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
        unordered_map<int, int> position;

        for (int i = 0; i < nums.size(); i++) {
            position[nums[i]] = i;
        }

        for (auto& operation : operations) {
            int oldValue = operation[0];
            int newValue = operation[1];

            int index = position[oldValue];

            nums[index] = newValue;

            position.erase(oldValue);
            position[newValue] = index;
        }

        return nums;
    }
};
```

### JavaScript
```javascript
var arrayChange = function(nums, operations) {
    const position = new Map();

    for (let i = 0; i < nums.length; i++) {
        position.set(nums[i], i);
    }

    for (const [oldValue, newValue] of operations) {
        const index = position.get(oldValue);

        nums[index] = newValue;

        position.delete(oldValue);
        position.set(newValue, index);
    }

    return nums;
};
```

### Go
```go
func arrayChange(nums []int, operations [][]int) []int {
    position := make(map[int]int)

    for i, value := range nums {
        position[value] = i
    }

    for _, operation := range operations {
        oldValue := operation[0]
        newValue := operation[1]

        index := position[oldValue]

        nums[index] = newValue

        delete(position, oldValue)
        position[newValue] = index
    }

    return nums
}
```

### Ruby
```ruby
def array_change(nums, operations)
  position = {}

  nums.each_with_index do |value, index|
    position[value] = index
  end

  operations.each do |old_value, new_value|
    index = position[old_value]

    nums[index] = new_value

    position.delete(old_value)
    position[new_value] = index
  end

  nums
end
```

### PHP
```php
class Solution {

    function arrayChange($nums, $operations) {
        $position = [];

        foreach ($nums as $index => $value) {
            $position[$value] = $index;
        }

        foreach ($operations as $operation) {
            $oldValue = $operation[0];
            $newValue = $operation[1];

            $index = $position[$oldValue];

            $nums[$index] = $newValue;

            unset($position[$oldValue]);
            $position[$newValue] = $index;
        }

        return $nums;
    }
}
```
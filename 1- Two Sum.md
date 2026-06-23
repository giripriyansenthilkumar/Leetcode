# Intuition
For each number in the array, we need to find another number such that their sum equals the target.

Instead of checking every pair of elements, we can store previously seen numbers in a hash map. For the current number `nums[i]`, we calculate its required complement `target - nums[i]`. If this complement has already been seen, we have found the answer.

# Approach
1. Initialize a hash map to store numbers and their indices.
2. Traverse the array:
   - Compute the complement as `target - nums[i]`.
   - Check if the complement exists in the hash map.
     - If it does, return the stored index and the current index.
   - Otherwise, store the current number and its index in the hash map.
3. Since exactly one valid answer exists, the pair will be found during the traversal.

# Complexity
- Time complexity: **O(n)**
  - Each element is processed once, and hash map operations take O(1) on average.

- Space complexity: **O(n)**
  - In the worst case, all elements are stored in the hash map.

# Code

### Python
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index in range(len(nums)):
            complement = target - nums[index]

            if complement in index_map:
                return [index_map[complement], index]

            index_map[nums[index]] = index
```

### Java
```java
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (indexMap.containsKey(complement)) {
                return new int[]{indexMap.get(complement), i};
            }

            indexMap.put(nums[i], i);
        }

        return new int[]{};
    }
}
```

### C++
```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indexMap;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (indexMap.count(complement)) {
                return {indexMap[complement], i};
            }

            indexMap[nums[i]] = i;
        }

        return {};
    }
};
```

### C
```c
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }

    return NULL;
}
```

### JavaScript
```javascript
var twoSum = function(nums, target) {
    const indexMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (indexMap.has(complement)) {
            return [indexMap.get(complement), i];
        }

        indexMap.set(nums[i], i);
    }
};
```

### Go
```go
func twoSum(nums []int, target int) []int {
    indexMap := make(map[int]int)

    for i, num := range nums {
        complement := target - num

        if index, exists := indexMap[complement]; exists {
            return []int{index, i}
        }

        indexMap[num] = i
    }

    return []int{}
}
```

### Ruby
```ruby
def two_sum(nums, target)
  index_map = {}

  nums.each_with_index do |num, index|
    complement = target - num

    if index_map.key?(complement)
      return [index_map[complement], index]
    end

    index_map[num] = index
  end
end
```

### PHP
```php
class Solution {

    function twoSum($nums, $target) {
        $indexMap = [];

        foreach ($nums as $index => $num) {
            $complement = $target - $num;

            if (isset($indexMap[$complement])) {
                return [$indexMap[$complement], $index];
            }

            $indexMap[$num] = $index;
        }

        return [];
    }
}
```
# Intuition
To find the `k` most frequent elements, we first count how many times each number appears in the array.

Once the frequencies are known, we sort the unique elements based on their frequency in descending order and return the first `k` elements from the sorted list.

# Approach
1. Traverse the array and store the frequency of each number in a hash map.
2. Sort the keys of the hash map based on their frequencies in descending order.
3. Return the first `k` elements from the sorted result.

# Complexity
- Time complexity: **O(n log n)**
  - Building the frequency map takes **O(n)**.
  - Sorting the unique elements takes **O(m log m)**, where `m` is the number of distinct elements.
  - In the worst case, `m = n`.

- Space complexity: **O(n)**
  - The frequency map stores all distinct elements.

# Code

### Python
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1

        sorted_elements = sorted(
            frequency_map,
            key=frequency_map.get,
            reverse=True
        )

        return sorted_elements[:k]
```

### Java
```java
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();

        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        List<Integer> elements = new ArrayList<>(frequencyMap.keySet());

        elements.sort((a, b) ->
            frequencyMap.get(b) - frequencyMap.get(a)
        );

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = elements.get(i);
        }

        return result;
    }
}
```

### C++
```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencyMap;

        for (int num : nums) {
            frequencyMap[num]++;
        }

        vector<int> elements;

        for (auto& entry : frequencyMap) {
            elements.push_back(entry.first);
        }

        sort(elements.begin(), elements.end(),
            [&](int a, int b) {
                return frequencyMap[a] > frequencyMap[b];
            });

        return vector<int>(elements.begin(), elements.begin() + k);
    }
};
```

### JavaScript
```javascript
var topKFrequent = function(nums, k) {
    const frequencyMap = new Map();

    for (const num of nums) {
        frequencyMap.set(
            num,
            (frequencyMap.get(num) || 0) + 1
        );
    }

    return [...frequencyMap.keys()]
        .sort((a, b) => frequencyMap.get(b) - frequencyMap.get(a))
        .slice(0, k);
};
```

### Go
```go
import "sort"

func topKFrequent(nums []int, k int) []int {
    frequencyMap := make(map[int]int)

    for _, num := range nums {
        frequencyMap[num]++
    }

    elements := make([]int, 0)

    for num := range frequencyMap {
        elements = append(elements, num)
    }

    sort.Slice(elements, func(i, j int) bool {
        return frequencyMap[elements[i]] > frequencyMap[elements[j]]
    })

    return elements[:k]
}
```

### Ruby
```ruby
def top_k_frequent(nums, k)
  frequency_map = Hash.new(0)

  nums.each do |num|
    frequency_map[num] += 1
  end

  frequency_map
    .sort_by { |_, frequency| -frequency }
    .first(k)
    .map(&:first)
end
```

### PHP
```php
class Solution {

    function topKFrequent($nums, $k) {
        $frequencyMap = [];

        foreach ($nums as $num) {
            if (!isset($frequencyMap[$num])) {
                $frequencyMap[$num] = 1;
            } else {
                $frequencyMap[$num]++;
            }
        }

        arsort($frequencyMap);

        return array_slice(
            array_keys($frequencyMap),
            0,
            $k
        );
    }
}
```
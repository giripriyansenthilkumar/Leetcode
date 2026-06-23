# Intuition
A consecutive sequence can only start from a number whose predecessor is not present in the array.

By storing all numbers in a hash set, we can check the existence of elements in O(1) time. For each potential sequence start, we extend the sequence forward until the consecutive pattern breaks, keeping track of the maximum length found.

# Approach
1. Convert the array into a set for O(1) lookups.
2. Iterate through each number in the set.
3. Identify the start of a sequence:
   - If `num - 1` is not in the set, then `num` is the beginning of a consecutive sequence.
4. Count the length of the sequence by checking consecutive numbers.
5. Update the maximum sequence length.
6. Return the maximum length found.

# Complexity
- Time complexity: **O(n)**
  - Each number is visited at most once while extending sequences.

- Space complexity: **O(n)**
  - The hash set stores all unique numbers.

# Code

### Python
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_length = 0

        for num in numbers:
            if num - 1 not in numbers:
                current_length = 1

                while num + current_length in numbers:
                    current_length += 1

                longest_length = max(longest_length, current_length)

        return longest_length
```

### Java
```java
import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numbers = new HashSet<>();

        for (int num : nums) {
            numbers.add(num);
        }

        int longestLength = 0;

        for (int num : numbers) {
            if (!numbers.contains(num - 1)) {
                int currentLength = 1;

                while (numbers.contains(num + currentLength)) {
                    currentLength++;
                }

                longestLength = Math.max(longestLength, currentLength);
            }
        }

        return longestLength;
    }
}
```

### C++
```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numbers(nums.begin(), nums.end());

        int longestLength = 0;

        for (int num : numbers) {
            if (!numbers.count(num - 1)) {
                int currentLength = 1;

                while (numbers.count(num + currentLength)) {
                    currentLength++;
                }

                longestLength = max(longestLength, currentLength);
            }
        }

        return longestLength;
    }
};
```

### JavaScript
```javascript
var longestConsecutive = function(nums) {
    const numbers = new Set(nums);
    let longestLength = 0;

    for (const num of numbers) {
        if (!numbers.has(num - 1)) {
            let currentLength = 1;

            while (numbers.has(num + currentLength)) {
                currentLength++;
            }

            longestLength = Math.max(longestLength, currentLength);
        }
    }

    return longestLength;
};
```

### Go
```go
func longestConsecutive(nums []int) int {
    numbers := make(map[int]bool)

    for _, num := range nums {
        numbers[num] = true
    }

    longestLength := 0

    for num := range numbers {
        if !numbers[num-1] {
            currentLength := 1

            for numbers[num+currentLength] {
                currentLength++
            }

            if currentLength > longestLength {
                longestLength = currentLength
            }
        }
    }

    return longestLength
}
```

### Ruby
```ruby
def longest_consecutive(nums)
  numbers = nums.to_set
  longest_length = 0

  numbers.each do |num|
    unless numbers.include?(num - 1)
      current_length = 1

      while numbers.include?(num + current_length)
        current_length += 1
      end

      longest_length = [longest_length, current_length].max
    end
  end

  longest_length
end
```

### PHP
```php
class Solution {

    function longestConsecutive($nums) {
        $numbers = array_flip($nums);
        $longestLength = 0;

        foreach ($numbers as $num => $_) {
            if (!isset($numbers[$num - 1])) {
                $currentLength = 1;

                while (isset($numbers[$num + $currentLength])) {
                    $currentLength++;
                }

                $longestLength = max($longestLength, $currentLength);
            }
        }

        return $longestLength;
    }
}
```
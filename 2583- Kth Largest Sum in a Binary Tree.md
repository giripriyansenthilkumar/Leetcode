# Intuition
We need the sum of values at each level of the binary tree and then find the K-th largest among those sums.

A level-order traversal (BFS) naturally processes the tree level by level. For each level, we compute its sum and store it. After collecting all level sums, we sort them in descending order and return the K-th largest sum.

# Approach
1. Use a queue to perform BFS.
2. For each level:
   - Process all nodes currently in the queue.
   - Compute the sum of their values.
   - Add their children to the queue.
   - Store the level sum.
3. After traversing the tree:
   - If the number of levels is less than `k`, return `-1`.
   - Otherwise, sort the level sums in descending order.
   - Return the element at index `k - 1`.

# Complexity
- Time complexity: **O(n + L log L)**
  - `O(n)` for BFS traversal of all nodes.
  - `O(L log L)` for sorting level sums, where `L` is the number of levels.

- Space complexity: **O(n)**
  - Queue and level sums array.

# Code

### Python
```python
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []

        if root is None:
            return -1

        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_sum = 0

            for _ in range(level_size):
                node = queue.popleft()

                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_sums.append(current_sum)

        if len(level_sums) < k:
            return -1

        level_sums.sort(reverse=True)

        return level_sums[k - 1]
```

### Java
```java
class Solution {
    public long kthLargestLevelSum(TreeNode root, int k) {
        List<Long> levelSums = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            long currentSum = 0;

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();

                currentSum += node.val;

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            levelSums.add(currentSum);
        }

        if (levelSums.size() < k) {
            return -1;
        }

        levelSums.sort(Collections.reverseOrder());

        return levelSums.get(k - 1);
    }
}
```

### C++
```cpp
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> levelSums;
        queue<TreeNode*> q;

        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            long long currentSum = 0;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                currentSum += node->val;

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            levelSums.push_back(currentSum);
        }

        if (levelSums.size() < k) {
            return -1;
        }

        sort(levelSums.begin(), levelSums.end(), greater<long long>());

        return levelSums[k - 1];
    }
};
```

### JavaScript
```javascript
var kthLargestLevelSum = function(root, k) {
    const levelSums = [];
    const queue = [root];

    while (queue.length) {
        const size = queue.length;
        let currentSum = 0;

        for (let i = 0; i < size; i++) {
            const node = queue.shift();

            currentSum += node.val;

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        levelSums.push(currentSum);
    }

    if (levelSums.length < k) {
        return -1;
    }

    levelSums.sort((a, b) => b - a);

    return levelSums[k - 1];
};
```

### Go
```go
func kthLargestLevelSum(root *TreeNode, k int) int64 {
    levelSums := []int64{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        size := len(queue)
        var currentSum int64 = 0

        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]

            currentSum += int64(node.Val)

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        levelSums = append(levelSums, currentSum)
    }

    if len(levelSums) < k {
        return -1
    }

    sort.Slice(levelSums, func(i, j int) bool {
        return levelSums[i] > levelSums[j]
    })

    return levelSums[k-1]
}
```

### Ruby
```ruby
def kth_largest_level_sum(root, k)
  level_sums = []
  queue = [root]

  until queue.empty?
    size = queue.length
    current_sum = 0

    size.times do
      node = queue.shift

      current_sum += node.val

      queue << node.left if node.left
      queue << node.right if node.right
    end

    level_sums << current_sum
  end

  return -1 if level_sums.length < k

  level_sums.sort!.reverse!

  level_sums[k - 1]
end
```

### PHP
```php
class Solution {

    function kthLargestLevelSum($root, $k) {
        $levelSums = [];
        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);
            $currentSum = 0;

            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);

                $currentSum += $node->val;

                if ($node->left) {
                    $queue[] = $node->left;
                }

                if ($node->right) {
                    $queue[] = $node->right;
                }
            }

            $levelSums[] = $currentSum;
        }

        if (count($levelSums) < $k) {
            return -1;
        }

        rsort($levelSums);

        return $levelSums[$k - 1];
    }
}
```
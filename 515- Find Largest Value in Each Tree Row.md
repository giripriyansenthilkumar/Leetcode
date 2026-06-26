# Intuition
We need to find the largest value present at each level of the binary tree.

A level-order traversal (BFS) processes nodes level by level. While traversing a level, we keep track of the maximum value among all nodes in that level. After finishing the level, we store the maximum value in the result.

# Approach
1. If the tree is empty, return an empty list.
2. Use a queue to perform BFS.
3. For each level:
   - Initialize a variable to store the maximum value of the current level.
   - Process all nodes at that level.
   - Update the maximum value while visiting nodes.
   - Add the children of each node to the queue.
4. Append the maximum value of each level to the result.
5. Return the result list.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited exactly once.

- Space complexity: **O(w)**
  - Where `w` is the maximum width of the tree.
  - In the worst case, this can be **O(n)**.

# Code

### Python
```python
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_max = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()

                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_max)

        return result
```

### Java
```java
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            int levelMax = Integer.MIN_VALUE;

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();

                levelMax = Math.max(levelMax, node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(levelMax);
        }

        return result;
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int> result;

        if (!root) {
            return result;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            int levelMax = INT_MIN;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                levelMax = max(levelMax, node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            result.push_back(levelMax);
        }

        return result;
    }
};
```

### JavaScript
```javascript
var largestValues = function(root) {
    if (!root) {
        return [];
    }

    const result = [];
    const queue = [root];

    while (queue.length) {
        const size = queue.length;
        let levelMax = -Infinity;

        for (let i = 0; i < size; i++) {
            const node = queue.shift();

            levelMax = Math.max(levelMax, node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        result.push(levelMax);
    }

    return result;
};
```

### Go
```go
func largestValues(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }

    result := []int{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        size := len(queue)
        levelMax := math.MinInt

        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]

            if node.Val > levelMax {
                levelMax = node.Val
            }

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        result = append(result, levelMax)
    }

    return result
}
```

### Ruby
```ruby
def largest_values(root)
  return [] if root.nil?

  result = []
  queue = [root]

  until queue.empty?
    size = queue.length
    level_max = -Float::INFINITY

    size.times do
      node = queue.shift

      level_max = [level_max, node.val].max

      queue << node.left if node.left
      queue << node.right if node.right
    end

    result << level_max
  end

  result
end
```

### PHP
```php
class Solution {

    function largestValues($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);
            $levelMax = PHP_INT_MIN;

            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);

                $levelMax = max($levelMax, $node->val);

                if ($node->left) {
                    $queue[] = $node->left;
                }

                if ($node->right) {
                    $queue[] = $node->right;
                }
            }

            $result[] = $levelMax;
        }

        return $result;
    }
}
```
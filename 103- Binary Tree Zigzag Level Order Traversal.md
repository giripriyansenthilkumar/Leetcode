# Intuition
A normal level-order traversal (BFS) visits the tree level by level from left to right.

To obtain the zigzag order, we first collect the nodes of each level using BFS. Afterward, we reverse the values of every alternate level (starting from the second level) to achieve the required left-to-right and right-to-left pattern.

# Approach
1. If the tree is empty, return an empty list.
2. Perform a BFS traversal using a queue.
3. For each level:
   - Process all nodes currently in the queue.
   - Store their values in a list.
   - Add their children to the queue.
   - Append the level values to the result.
4. Traverse the result and reverse every alternate level starting from index `1`.
5. Return the modified result.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited exactly once.
  - Reversing alternate levels together also takes linear time.

- Space complexity: **O(n)**
  - The queue and the result list together store all nodes.

# Code

### Python
```python
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        level = 1

        while level < len(result):
            result[level].reverse()
            level += 2

        return result
```

### Java
```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();

                currentLevel.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);
        }

        for (int i = 1; i < result.size(); i += 2) {
            Collections.reverse(result.get(i));
        }

        return result;
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;

        if (!root) {
            return result;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            vector<int> currentLevel;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                currentLevel.push_back(node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            result.push_back(currentLevel);
        }

        for (int i = 1; i < result.size(); i += 2) {
            reverse(result[i].begin(), result[i].end());
        }

        return result;
    }
};
```

### JavaScript
```javascript
var zigzagLevelOrder = function(root) {
    if (!root) {
        return [];
    }

    const result = [];
    const queue = [root];

    while (queue.length) {
        const size = queue.length;
        const currentLevel = [];

        for (let i = 0; i < size; i++) {
            const node = queue.shift();

            currentLevel.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        result.push(currentLevel);
    }

    for (let i = 1; i < result.length; i += 2) {
        result[i].reverse();
    }

    return result;
};
```

### Go
```go
func zigzagLevelOrder(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }

    result := [][]int{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        size := len(queue)
        currentLevel := []int{}

        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]

            currentLevel = append(currentLevel, node.Val)

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        result = append(result, currentLevel)
    }

    for i := 1; i < len(result); i += 2 {
        for left, right := 0, len(result[i])-1; left < right; left, right = left+1, right-1 {
            result[i][left], result[i][right] = result[i][right], result[i][left]
        }
    }

    return result
}
```

### Ruby
```ruby
def zigzag_level_order(root)
  return [] if root.nil?

  result = []
  queue = [root]

  until queue.empty?
    size = queue.length
    current_level = []

    size.times do
      node = queue.shift

      current_level << node.val

      queue << node.left if node.left
      queue << node.right if node.right
    end

    result << current_level
  end

  (1...result.length).step(2) do |i|
    result[i].reverse!
  end

  result
end
```

### PHP
```php
class Solution {

    function zigzagLevelOrder($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);
            $currentLevel = [];

            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);

                $currentLevel[] = $node->val;

                if ($node->left) {
                    $queue[] = $node->left;
                }

                if ($node->right) {
                    $queue[] = $node->right;
                }
            }

            $result[] = $currentLevel;
        }

        for ($i = 1; $i < count($result); $i += 2) {
            $result[$i] = array_reverse($result[$i]);
        }

        return $result;
    }
}
```
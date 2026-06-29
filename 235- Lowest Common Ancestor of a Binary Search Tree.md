# Intuition
We need to find all root-to-leaf paths whose sum of node values equals the given target.

A Depth-First Search (DFS) allows us to explore every root-to-leaf path. While traversing, we maintain the current path. Whenever we reach a leaf node, we check if the sum of the path equals the target. If it does, we store a copy of the current path. After exploring a branch, we backtrack by removing the last node so the path can be reused for other branches.

# Approach
1. Perform a DFS traversal starting from the root.
2. Maintain a list representing the current root-to-node path.
3. At each node:
   - Add the node's value to the current path.
4. If the node is a leaf:
   - Check whether the sum of the current path equals the target.
   - If it does, add a copy of the path to the result.
5. Recursively traverse the left and right subtrees.
6. Remove the current node from the path before returning (backtracking).
7. Return all valid paths.

# Complexity
- Time complexity: **O(n × h)**
  - Every node is visited once, and computing `sum(path)` at each leaf takes up to `O(h)`, where `h` is the tree height.

- Space complexity: **O(h)**
  - The recursion stack and current path store at most one root-to-leaf path.

# Code

### Python
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, target, path):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                if sum(path) == target:
                    result.append(path.copy())

                path.pop()
                return

            dfs(node.left, target, path)
            dfs(node.right, target, path)

            path.pop()

        dfs(root, targetSum, [])

        return result
```

### Java
```java
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum, new ArrayList<>());
        return result;
    }

    private void dfs(TreeNode node, int target, List<Integer> path) {
        if (node == null) {
            return;
        }

        path.add(node.val);

        if (node.left == null && node.right == null) {
            int sum = 0;

            for (int value : path) {
                sum += value;
            }

            if (sum == target) {
                result.add(new ArrayList<>(path));
            }

            path.remove(path.size() - 1);
            return;
        }

        dfs(node.left, target, path);
        dfs(node.right, target, path);

        path.remove(path.size() - 1);
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<vector<int>> result;

    void dfs(TreeNode* node, int target, vector<int>& path) {
        if (node == nullptr) {
            return;
        }

        path.push_back(node->val);

        if (node->left == nullptr && node->right == nullptr) {
            int sum = 0;

            for (int value : path) {
                sum += value;
            }

            if (sum == target) {
                result.push_back(path);
            }

            path.pop_back();
            return;
        }

        dfs(node->left, target, path);
        dfs(node->right, target, path);

        path.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        dfs(root, targetSum, path);
        return result;
    }
};
```

### JavaScript
```javascript
var pathSum = function(root, targetSum) {
    const result = [];

    function dfs(node, path) {
        if (!node) {
            return;
        }

        path.push(node.val);

        if (!node.left && !node.right) {
            const sum = path.reduce((a, b) => a + b, 0);

            if (sum === targetSum) {
                result.push([...path]);
            }

            path.pop();
            return;
        }

        dfs(node.left, path);
        dfs(node.right, path);

        path.pop();
    }

    dfs(root, []);

    return result;
};
```

### Go
```go
func pathSum(root *TreeNode, targetSum int) [][]int {
    result := [][]int{}

    var dfs func(*TreeNode, []int)

    dfs = func(node *TreeNode, path []int) {
        if node == nil {
            return
        }

        path = append(path, node.Val)

        if node.Left == nil && node.Right == nil {
            sum := 0

            for _, value := range path {
                sum += value
            }

            if sum == targetSum {
                temp := append([]int{}, path...)
                result = append(result, temp)
            }

            return
        }

        dfs(node.Left, path)
        dfs(node.Right, path)
    }

    dfs(root, []int{})

    return result
}
```

### Ruby
```ruby
def path_sum(root, target_sum)
  result = []

  dfs = lambda do |node, path|
    return if node.nil?

    path << node.val

    if node.left.nil? && node.right.nil?
      result << path.clone if path.sum == target_sum
      path.pop
      return
    end

    dfs.call(node.left, path)
    dfs.call(node.right, path)

    path.pop
  end

  dfs.call(root, [])

  result
end
```

### PHP
```php
class Solution {

    private $result = [];

    function pathSum($root, $targetSum) {
        $this->dfs($root, $targetSum, []);
        return $this->result;
    }

    private function dfs($node, $target, $path) {
        if ($node === null) {
            return;
        }

        $path[] = $node->val;

        if ($node->left === null && $node->right === null) {
            if (array_sum($path) == $target) {
                $this->result[] = $path;
            }

            return;
        }

        $this->dfs($node->left, $target, $path);
        $this->dfs($node->right, $target, $path);
    }
}
```
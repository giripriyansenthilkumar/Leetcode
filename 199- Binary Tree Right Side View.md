# Intuition
The right side view contains the node that is visible when looking at the tree from the right side.

If we perform a DFS traversal and always visit the right child before the left child, then the first node encountered at each depth will be the rightmost node of that level. We store this first node for every depth and return the collected values.

# Approach
1. Create a dictionary to store the first node seen at each depth.
2. Perform a DFS traversal:
   - Visit the current node.
   - If the current depth has not been seen before, store the node's value.
   - Traverse the right subtree first.
   - Traverse the left subtree afterward.
3. Since right nodes are visited first, the first node stored at each depth is the visible node from the right side.
4. Return the dictionary values.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited exactly once.

- Space complexity: **O(h)**
  - Recursive call stack, where `h` is the height of the tree.
  - In the worst case (skewed tree), `O(n)`.

# Code

### Python
```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth_map = {}

        def dfs(node, depth):
            if node is None:
                return

            if depth not in depth_map:
                depth_map[depth] = node.val

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return list(depth_map.values())
```

### Java
```java
class Solution {
    private Map<Integer, Integer> depthMap = new HashMap<>();

    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, 0);
        return new ArrayList<>(depthMap.values());
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        if (!depthMap.containsKey(depth)) {
            depthMap.put(depth, node.val);
        }

        dfs(node.right, depth + 1);
        dfs(node.left, depth + 1);
    }
}
```

### C++
```cpp
class Solution {
public:
    unordered_map<int, int> depthMap;

    void dfs(TreeNode* node, int depth) {
        if (node == nullptr) {
            return;
        }

        if (!depthMap.count(depth)) {
            depthMap[depth] = node->val;
        }

        dfs(node->right, depth + 1);
        dfs(node->left, depth + 1);
    }

    vector<int> rightSideView(TreeNode* root) {
        dfs(root, 0);

        vector<int> result;

        for (int i = 0; i < depthMap.size(); i++) {
            result.push_back(depthMap[i]);
        }

        return result;
    }
};
```

### JavaScript
```javascript
var rightSideView = function(root) {
    const depthMap = {};

    function dfs(node, depth) {
        if (!node) {
            return;
        }

        if (!(depth in depthMap)) {
            depthMap[depth] = node.val;
        }

        dfs(node.right, depth + 1);
        dfs(node.left, depth + 1);
    }

    dfs(root, 0);

    return Object.values(depthMap);
};
```

### Go
```go
func rightSideView(root *TreeNode) []int {
    depthMap := make(map[int]int)

    var dfs func(*TreeNode, int)

    dfs = func(node *TreeNode, depth int) {
        if node == nil {
            return
        }

        if _, exists := depthMap[depth]; !exists {
            depthMap[depth] = node.Val
        }

        dfs(node.Right, depth+1)
        dfs(node.Left, depth+1)
    }

    dfs(root, 0)

    result := []int{}

    for i := 0; i < len(depthMap); i++ {
        result = append(result, depthMap[i])
    }

    return result
}
```

### Ruby
```ruby
def right_side_view(root)
  depth_map = {}

  dfs = lambda do |node, depth|
    return if node.nil?

    depth_map[depth] = node.val unless depth_map.key?(depth)

    dfs.call(node.right, depth + 1)
    dfs.call(node.left, depth + 1)
  end

  dfs.call(root, 0)

  depth_map.values
end
```

### PHP
```php
class Solution {

    private $depthMap = [];

    function rightSideView($root) {
        $this->dfs($root, 0);
        return array_values($this->depthMap);
    }

    private function dfs($node, $depth) {
        if ($node === null) {
            return;
        }

        if (!isset($this->depthMap[$depth])) {
            $this->depthMap[$depth] = $node->val;
        }

        $this->dfs($node->right, $depth + 1);
        $this->dfs($node->left, $depth + 1);
    }
}
```
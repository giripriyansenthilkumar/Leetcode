# Intuition
We need to determine whether there exists a root-to-leaf path whose node values add up to the given target sum.

We can use Depth-First Search (DFS) to traverse every root-to-leaf path while maintaining the current path sum. Whenever we reach a leaf node, we compare the accumulated sum with the target. If they are equal, we have found a valid path.

# Approach
1. Perform a DFS traversal starting from the root.
2. Keep track of the sum of node values along the current path.
3. For each node:
   - Add its value to the current sum.
   - If it is a leaf node, check whether the current sum equals the target.
4. Recursively search the left and right subtrees.
5. If either subtree contains a valid path, return `True`; otherwise, return `False`.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited at most once.

- Space complexity: **O(h)**
  - Due to the recursion stack, where `h` is the height of the tree.
  - Worst case: **O(n)** for a skewed tree.

# Code

### Python
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(node, target, current_sum):
            if node is None:
                return False

            current_sum += node.val

            if node.left is None and node.right is None:
                return current_sum == target

            return (
                has_sum(node.left, target, current_sum) or
                has_sum(node.right, target, current_sum)
            )

        return has_sum(root, targetSum, 0)
```

### Java
```java
class Solution {

    public boolean hasPathSum(TreeNode root, int targetSum) {
        return hasSum(root, targetSum, 0);
    }

    private boolean hasSum(TreeNode node, int target, int currentSum) {
        if (node == null) {
            return false;
        }

        currentSum += node.val;

        if (node.left == null && node.right == null) {
            return currentSum == target;
        }

        return hasSum(node.left, target, currentSum) ||
               hasSum(node.right, target, currentSum);
    }
}
```

### C++
```cpp
class Solution {
public:
    bool hasSum(TreeNode* node, int target, int currentSum) {
        if (node == nullptr) {
            return false;
        }

        currentSum += node->val;

        if (node->left == nullptr && node->right == nullptr) {
            return currentSum == target;
        }

        return hasSum(node->left, target, currentSum) ||
               hasSum(node->right, target, currentSum);
    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        return hasSum(root, targetSum, 0);
    }
};
```

### JavaScript
```javascript
var hasPathSum = function(root, targetSum) {

    function hasSum(node, target, currentSum) {
        if (!node) {
            return false;
        }

        currentSum += node.val;

        if (!node.left && !node.right) {
            return currentSum === target;
        }

        return hasSum(node.left, target, currentSum) ||
               hasSum(node.right, target, currentSum);
    }

    return hasSum(root, targetSum, 0);
};
```

### Go
```go
func hasPathSum(root *TreeNode, targetSum int) bool {

    var hasSum func(*TreeNode, int) bool

    hasSum = func(node *TreeNode, currentSum int) bool {
        if node == nil {
            return false
        }

        currentSum += node.Val

        if node.Left == nil && node.Right == nil {
            return currentSum == targetSum
        }

        return hasSum(node.Left, currentSum) ||
               hasSum(node.Right, currentSum)
    }

    return hasSum(root, 0)
}
```

### Ruby
```ruby
def has_path_sum(root, target_sum)

  has_sum = lambda do |node, current_sum|
    return false if node.nil?

    current_sum += node.val

    if node.left.nil? && node.right.nil?
      return current_sum == target_sum
    end

    has_sum.call(node.left, current_sum) ||
    has_sum.call(node.right, current_sum)
  end

  has_sum.call(root, 0)
end
```

### PHP
```php
class Solution {

    function hasPathSum($root, $targetSum) {
        return $this->hasSum($root, $targetSum, 0);
    }

    private function hasSum($node, $target, $currentSum) {
        if ($node === null) {
            return false;
        }

        $currentSum += $node->val;

        if ($node->left === null && $node->right === null) {
            return $currentSum == $target;
        }

        return $this->hasSum($node->left, $target, $currentSum) ||
               $this->hasSum($node->right, $target, $currentSum);
    }
}
```
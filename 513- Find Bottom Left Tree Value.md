# Intuition
We need to find the leftmost value in the last row of the tree.

By performing a DFS traversal and visiting the left subtree before the right subtree, the first node encountered at each new depth will be the leftmost node of that level. Whenever we reach a depth greater than any previously seen depth, we update the answer.

# Approach
1. Maintain:
   - `depth` = maximum depth visited so far.
   - `answer` = leftmost value at the deepest level.
2. Perform a DFS traversal starting from the root.
3. For each node:
   - If its depth is greater than the current maximum depth:
     - Update the maximum depth.
     - Update the answer with the current node's value.
4. Traverse the left child before the right child.
5. Return the stored answer after the traversal completes.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited exactly once.

- Space complexity: **O(h)**
  - Due to the recursion stack, where `h` is the height of the tree.
  - Worst case: **O(n)** for a skewed tree.

# Code

```python []
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        answer = root.val

        def dfs(node, depth):
            nonlocal max_depth, answer

            if node is None:
                return

            if depth > max_depth:
                max_depth = depth
                answer = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return answer
```

```java []
class Solution {
    private int maxDepth = 0;
    private int answer;

    public int findBottomLeftValue(TreeNode root) {
        answer = root.val;
        dfs(root, 0);
        return answer;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        if (depth > maxDepth) {
            maxDepth = depth;
            answer = node.val;
        }

        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
    }
}
```

```cpp []
class Solution {
public:
    int maxDepth = 0;
    int answer;

    void dfs(TreeNode* node, int depth) {
        if (node == nullptr) {
            return;
        }

        if (depth > maxDepth) {
            maxDepth = depth;
            answer = node->val;
        }

        dfs(node->left, depth + 1);
        dfs(node->right, depth + 1);
    }

    int findBottomLeftValue(TreeNode* root) {
        answer = root->val;
        dfs(root, 0);
        return answer;
    }
};
```

```javascript []
var findBottomLeftValue = function(root) {
    let maxDepth = 0;
    let answer = root.val;

    function dfs(node, depth) {
        if (!node) {
            return;
        }

        if (depth > maxDepth) {
            maxDepth = depth;
            answer = node.val;
        }

        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
    }

    dfs(root, 0);

    return answer;
};
```

```go []
func findBottomLeftValue(root *TreeNode) int {
    maxDepth := 0
    answer := root.Val

    var dfs func(*TreeNode, int)

    dfs = func(node *TreeNode, depth int) {
        if node == nil {
            return
        }

        if depth > maxDepth {
            maxDepth = depth
            answer = node.Val
        }

        dfs(node.Left, depth+1)
        dfs(node.Right, depth+1)
    }

    dfs(root, 0)

    return answer
}
```

```ruby []
def find_bottom_left_value(root)
  max_depth = 0
  answer = root.val

  dfs = lambda do |node, depth|
    return if node.nil?

    if depth > max_depth
      max_depth = depth
      answer = node.val
    end

    dfs.call(node.left, depth + 1)
    dfs.call(node.right, depth + 1)
  end

  dfs.call(root, 0)

  answer
end
```

```php []
class Solution {

    private $maxDepth = 0;
    private $answer;

    function findBottomLeftValue($root) {
        $this->answer = $root->val;
        $this->dfs($root, 0);
        return $this->answer;
    }

    private function dfs($node, $depth) {
        if ($node === null) {
            return;
        }

        if ($depth > $this->maxDepth) {
            $this->maxDepth = $depth;
            $this->answer = $node->val;
        }

        $this->dfs($node->left, $depth + 1);
        $this->dfs($node->right, $depth + 1);
    }
}
```
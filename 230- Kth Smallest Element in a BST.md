# Intuition
In a Binary Search Tree (BST), an inorder traversal visits nodes in ascending order.

Therefore, if we perform an inorder traversal and store the visited values, the resulting list will be sorted. The K-th smallest element will simply be located at index `k - 1` in this sorted sequence.

# Approach
1. Perform an inorder traversal of the BST.
2. Store the visited node values in a list.
3. Since inorder traversal of a BST produces values in sorted order:
   - Return the element at index `k - 1`.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited once during the inorder traversal.

- Space complexity: **O(n)**
  - The traversal stores all node values in a list.

# Code

### Python
```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        return values[k - 1]
```

### Java
```java
class Solution {
    private List<Integer> values = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        inorder(root);
        return values.get(k - 1);
    }

    private void inorder(TreeNode node) {
        if (node == null) {
            return;
        }

        inorder(node.left);
        values.add(node.val);
        inorder(node.right);
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<int> values;

    void inorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        inorder(node->left);
        values.push_back(node->val);
        inorder(node->right);
    }

    int kthSmallest(TreeNode* root, int k) {
        inorder(root);
        return values[k - 1];
    }
};
```

### JavaScript
```javascript
var kthSmallest = function(root, k) {
    const values = [];

    function inorder(node) {
        if (!node) {
            return;
        }

        inorder(node.left);
        values.push(node.val);
        inorder(node.right);
    }

    inorder(root);

    return values[k - 1];
};
```

### Go
```go
func kthSmallest(root *TreeNode, k int) int {
    values := []int{}

    var inorder func(*TreeNode)

    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }

        inorder(node.Left)
        values = append(values, node.Val)
        inorder(node.Right)
    }

    inorder(root)

    return values[k-1]
}
```

### Ruby
```ruby
def kth_smallest(root, k)
  values = []

  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    values << node.val
    inorder.call(node.right)
  end

  inorder.call(root)

  values[k - 1]
end
```

### PHP
```php
class Solution {

    private $values = [];

    function kthSmallest($root, $k) {
        $this->inorder($root);
        return $this->values[$k - 1];
    }

    private function inorder($node) {
        if ($node === null) {
            return;
        }

        $this->inorder($node->left);
        $this->values[] = $node->val;
        $this->inorder($node->right);
    }
}
```
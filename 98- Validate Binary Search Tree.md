# Intuition
A Binary Search Tree (BST) has the property that an inorder traversal visits nodes in strictly increasing order.

Therefore, if we perform an inorder traversal and collect the node values, the resulting sequence must be sorted in ascending order without duplicates. If any value is greater than or equal to the next value, the tree is not a valid BST.

# Approach
1. Perform an inorder traversal of the tree.
2. Store the visited node values in a list.
3. Traverse the list and check whether it is strictly increasing:
   - If `values[i] >= values[i + 1]`, return `False`.
4. If all adjacent pairs satisfy the BST property, return `True`.

# Complexity
- Time complexity: **O(n)**
  - Each node is visited exactly once.

- Space complexity: **O(n)**
  - The inorder traversal stores all node values in a list.

# Code

### Python
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            inorder_values.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(inorder_values) - 1):
            if inorder_values[i] >= inorder_values[i + 1]:
                return False

        return True
```

### Java
```java
class Solution {
    private List<Integer> inorderValues = new ArrayList<>();

    public boolean isValidBST(TreeNode root) {
        inorder(root);

        for (int i = 0; i < inorderValues.size() - 1; i++) {
            if (inorderValues.get(i) >= inorderValues.get(i + 1)) {
                return false;
            }
        }

        return true;
    }

    private void inorder(TreeNode node) {
        if (node == null) {
            return;
        }

        inorder(node.left);
        inorderValues.add(node.val);
        inorder(node.right);
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<int> inorderValues;

    void inorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        inorder(node->left);
        inorderValues.push_back(node->val);
        inorder(node->right);
    }

    bool isValidBST(TreeNode* root) {
        inorder(root);

        for (int i = 0; i < inorderValues.size() - 1; i++) {
            if (inorderValues[i] >= inorderValues[i + 1]) {
                return false;
            }
        }

        return true;
    }
};
```

### JavaScript
```javascript
var isValidBST = function(root) {
    const inorderValues = [];

    function inorder(node) {
        if (!node) {
            return;
        }

        inorder(node.left);
        inorderValues.push(node.val);
        inorder(node.right);
    }

    inorder(root);

    for (let i = 0; i < inorderValues.length - 1; i++) {
        if (inorderValues[i] >= inorderValues[i + 1]) {
            return false;
        }
    }

    return true;
};
```

### Go
```go
func isValidBST(root *TreeNode) bool {
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

    for i := 0; i < len(values)-1; i++ {
        if values[i] >= values[i+1] {
            return false
        }
    }

    return true
}
```

### Ruby
```ruby
def is_valid_bst(root)
  values = []

  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    values << node.val
    inorder.call(node.right)
  end

  inorder.call(root)

  (0...values.length - 1).each do |i|
    return false if values[i] >= values[i + 1]
  end

  true
end
```

### PHP
```php
class Solution {

    private $values = [];

    function isValidBST($root) {
        $this->inorder($root);

        for ($i = 0; $i < count($this->values) - 1; $i++) {
            if ($this->values[$i] >= $this->values[$i + 1]) {
                return false;
            }
        }

        return true;
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
````
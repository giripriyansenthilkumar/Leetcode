# Intuition
The flattened tree should follow the preorder traversal of the binary tree.

We first perform a preorder traversal and store all the visited nodes in a list. Since preorder already gives the required order, we reconnect each node so that its left pointer becomes `null` and its right pointer points to the next node in the preorder list.

# Approach
1. Perform a preorder traversal and store every visited node.
2. Traverse the stored list:
   - Set the current node's left pointer to `null`.
   - Set the current node's right pointer to the next node.
3. For the last node:
   - Set both its left and right pointers to `null`.

# Complexity
- **Time complexity:** **O(n)**
  - One preorder traversal and one pass to reconnect the nodes.

- **Space complexity:** **O(n)**
  - Stores all nodes in a list.

# Code

### Python
```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        nodes = []

        def preorder(node):
            if node is None:
                return

            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        nodes[-1].left = None
        nodes[-1].right = None
```

### Java
```java
class Solution {

    private List<TreeNode> nodes = new ArrayList<>();

    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        preorder(root);

        for (int i = 0; i < nodes.size() - 1; i++) {
            nodes.get(i).left = null;
            nodes.get(i).right = nodes.get(i + 1);
        }

        TreeNode last = nodes.get(nodes.size() - 1);
        last.left = null;
        last.right = null;
    }

    private void preorder(TreeNode node) {
        if (node == null) {
            return;
        }

        nodes.add(node);
        preorder(node.left);
        preorder(node.right);
    }
}
```

### C++
```cpp
class Solution {
public:
    vector<TreeNode*> nodes;

    void preorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        nodes.push_back(node);
        preorder(node->left);
        preorder(node->right);
    }

    void flatten(TreeNode* root) {
        if (root == nullptr) {
            return;
        }

        preorder(root);

        for (int i = 0; i < nodes.size() - 1; i++) {
            nodes[i]->left = nullptr;
            nodes[i]->right = nodes[i + 1];
        }

        nodes.back()->left = nullptr;
        nodes.back()->right = nullptr;
    }
};
```

### JavaScript
```javascript
var flatten = function(root) {
    if (!root) {
        return;
    }

    const nodes = [];

    function preorder(node) {
        if (!node) {
            return;
        }

        nodes.push(node);
        preorder(node.left);
        preorder(node.right);
    }

    preorder(root);

    for (let i = 0; i < nodes.length - 1; i++) {
        nodes[i].left = null;
        nodes[i].right = nodes[i + 1];
    }

    nodes[nodes.length - 1].left = null;
    nodes[nodes.length - 1].right = null;
};
```

### Go
```go
func flatten(root *TreeNode) {
    if root == nil {
        return
    }

    nodes := []*TreeNode{}

    var preorder func(*TreeNode)

    preorder = func(node *TreeNode) {
        if node == nil {
            return
        }

        nodes = append(nodes, node)
        preorder(node.Left)
        preorder(node.Right)
    }

    preorder(root)

    for i := 0; i < len(nodes)-1; i++ {
        nodes[i].Left = nil
        nodes[i].Right = nodes[i+1]
    }

    nodes[len(nodes)-1].Left = nil
    nodes[len(nodes)-1].Right = nil
}
```

### Ruby
```ruby
def flatten(root)
  return if root.nil?

  nodes = []

  preorder = lambda do |node|
    return if node.nil?

    nodes << node
    preorder.call(node.left)
    preorder.call(node.right)
  end

  preorder.call(root)

  (0...nodes.length - 1).each do |i|
    nodes[i].left = nil
    nodes[i].right = nodes[i + 1]
  end

  nodes[-1].left = nil
  nodes[-1].right = nil
end
```

### PHP
```php
class Solution {

    private $nodes = [];

    function flatten($root) {
        if ($root === null) {
            return;
        }

        $this->preorder($root);

        for ($i = 0; $i < count($this->nodes) - 1; $i++) {
            $this->nodes[$i]->left = null;
            $this->nodes[$i]->right = $this->nodes[$i + 1];
        }

        $last = count($this->nodes) - 1;
        $this->nodes[$last]->left = null;
        $this->nodes[$last]->right = null;
    }

    private function preorder($node) {
        if ($node === null) {
            return;
        }

        $this->nodes[] = $node;
        $this->preorder($node->left);
        $this->preorder($node->right);
    }
}
```
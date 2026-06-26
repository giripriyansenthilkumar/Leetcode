# Intuition
Each root-to-leaf path represents a number formed by concatenating the node values along the path.

We perform a DFS traversal while maintaining the current path. Whenever we reach a leaf node, we convert the collected path into a number and add it to the final sum. After exploring a path, we backtrack to correctly process other paths.

# Approach
1. Initialize a variable to store the final sum.
2. Perform a preorder DFS traversal.
3. Maintain a list containing the values along the current root-to-node path.
4. When a leaf node is reached:
   - Concatenate the values in the path to form a number.
   - Convert it to an integer and add it to the answer.
5. After visiting both children, remove the current node from the path (backtracking).
6. Return the accumulated sum.

# Complexity
- Time complexity: **O(n × h)**
  - `n` is the number of nodes and `h` is the height of the tree.
  - For each leaf, constructing the number from the stored path takes up to `O(h)` time.

- Space complexity: **O(h)**
  - The recursion stack and current path store at most one root-to-leaf path.

# Code

### Python
```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        path = []

        def preorder(node):
            nonlocal total_sum

            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                number = ""

                for digit in path:
                    number += str(digit)

                total_sum += int(number)

            preorder(node.left)
            preorder(node.right)

            path.pop()

        preorder(root)

        return total_sum
```

### Java
```java
class Solution {
    private int totalSum = 0;
    private List<Integer> path = new ArrayList<>();

    public int sumNumbers(TreeNode root) {
        preorder(root);
        return totalSum;
    }

    private void preorder(TreeNode node) {
        if (node == null) {
            return;
        }

        path.add(node.val);

        if (node.left == null && node.right == null) {
            StringBuilder number = new StringBuilder();

            for (int digit : path) {
                number.append(digit);
            }

            totalSum += Integer.parseInt(number.toString());
        }

        preorder(node.left);
        preorder(node.right);

        path.remove(path.size() - 1);
    }
}
```

### C++
```cpp
class Solution {
public:
    int totalSum = 0;
    vector<int> path;

    void preorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        path.push_back(node->val);

        if (node->left == nullptr && node->right == nullptr) {
            string number = "";

            for (int digit : path) {
                number += to_string(digit);
            }

            totalSum += stoi(number);
        }

        preorder(node->left);
        preorder(node->right);

        path.pop_back();
    }

    int sumNumbers(TreeNode* root) {
        preorder(root);
        return totalSum;
    }
};
```

### JavaScript
```javascript
var sumNumbers = function(root) {
    let totalSum = 0;
    const path = [];

    function preorder(node) {
        if (!node) {
            return;
        }

        path.push(node.val);

        if (!node.left && !node.right) {
            totalSum += Number(path.join(""));
        }

        preorder(node.left);
        preorder(node.right);

        path.pop();
    }

    preorder(root);

    return totalSum;
};
```

### Go
```go
import (
    "strconv"
    "strings"
)

func sumNumbers(root *TreeNode) int {
    totalSum := 0
    path := []int{}

    var preorder func(*TreeNode)

    preorder = func(node *TreeNode) {
        if node == nil {
            return
        }

        path = append(path, node.Val)

        if node.Left == nil && node.Right == nil {
            parts := []string{}

            for _, digit := range path {
                parts = append(parts, strconv.Itoa(digit))
            }

            number, _ := strconv.Atoi(strings.Join(parts, ""))
            totalSum += number
        }

        preorder(node.Left)
        preorder(node.Right)

        path = path[:len(path)-1]
    }

    preorder(root)

    return totalSum
}
```

### Ruby
```ruby
def sum_numbers(root)
  total_sum = 0
  path = []

  preorder = lambda do |node|
    return if node.nil?

    path << node.val

    if node.left.nil? && node.right.nil?
      total_sum += path.join.to_i
    end

    preorder.call(node.left)
    preorder.call(node.right)

    path.pop
  end

  preorder.call(root)

  total_sum
end
```

### PHP
```php
class Solution {

    private $totalSum = 0;
    private $path = [];

    function sumNumbers($root) {
        $this->preorder($root);
        return $this->totalSum;
    }

    private function preorder($node) {
        if ($node === null) {
            return;
        }

        $this->path[] = $node->val;

        if ($node->left === null && $node->right === null) {
            $this->totalSum += intval(implode("", $this->path));
        }

        $this->preorder($node->left);
        $this->preorder($node->right);

        array_pop($this->path);
    }
}
```
# Intuition
Nodes at the same level should be connected from left to right using their `next` pointers.

A level-order traversal (BFS) naturally processes the tree one level at a time. While traversing a level, each node can be connected to the next node in the queue, except for the last node of that level, whose `next` pointer remains `NULL`.

# Approach
1. If the tree is empty, return `None`.
2. Perform a BFS traversal using a queue.
3. For each level:
   - Process all nodes in the current level.
   - Add their left and right children to the queue.
   - If the current node is not the last node of the level, set its `next` pointer to the next node in the queue.
4. Return the root after all connections are established.

# Complexity
- Time complexity: **O(n)**
  - Every node is visited exactly once.

- Space complexity: **O(n)**
  - The queue stores nodes level by level.
  - For a perfect binary tree, the maximum queue size can be proportional to the number of nodes in the last level.

# Code

### Python
```python
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if i != level_size - 1:
                    node.next = queue[0]

        return root
```

### Java
```java
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return null;
        }

        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                Node node = queue.poll();

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }

                if (i != size - 1) {
                    node.next = queue.peek();
                }
            }
        }

        return root;
    }
}
```

### C++
```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr) {
            return nullptr;
        }

        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                Node* node = q.front();
                q.pop();

                if (node->left) {
                    q.push(node->left);
                }

                if (node->right) {
                    q.push(node->right);
                }

                if (i != size - 1) {
                    node->next = q.front();
                }
            }
        }

        return root;
    }
};
```

### JavaScript
```javascript
var connect = function(root) {
    if (!root) {
        return null;
    }

    const queue = [root];

    while (queue.length) {
        const size = queue.length;

        for (let i = 0; i < size; i++) {
            const node = queue.shift();

            if (node.left) {
                queue.push(node.left);
            }

            if (node.right) {
                queue.push(node.right);
            }

            if (i !== size - 1) {
                node.next = queue[0];
            }
        }
    }

    return root;
};
```

### Go
```go
func connect(root *Node) *Node {
    if root == nil {
        return nil
    }

    queue := []*Node{root}

    for len(queue) > 0 {
        size := len(queue)

        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }

            if i != size-1 {
                node.Next = queue[0]
            }
        }
    }

    return root
}
```

### Ruby
```ruby
def connect(root)
  return nil if root.nil?

  queue = [root]

  until queue.empty?
    size = queue.length

    size.times do |i|
      node = queue.shift

      queue << node.left if node.left
      queue << node.right if node.right

      node.next = queue.first if i != size - 1
    end
  end

  root
end
```

### PHP
```php
class Solution {

    function connect($root) {
        if ($root === null) {
            return null;
        }

        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);

            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);

                if ($node->left) {
                    $queue[] = $node->left;
                }

                if ($node->right) {
                    $queue[] = $node->right;
                }

                if ($i != $size - 1) {
                    $node->next = $queue[0];
                }
            }
        }

        return $root;
    }
}
```
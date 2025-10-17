class Solution:
    def connect(self, root):
        leftmost = root
        while leftmost and leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root


# perfect binary tree, use existing next pointers level by level, O(n) time

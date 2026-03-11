class Solution:
    def flatten(self, root) -> None:
        cur = root
        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


# rewire in place, push left subtree's rightmost to old right, O(n) time

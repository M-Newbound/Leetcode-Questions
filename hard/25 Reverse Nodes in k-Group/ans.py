class Solution:
    def reverseKGroup(self, head, k: int):
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        prev = self.reverseKGroup(node, k)
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


# there's probably a cleaner way to do this

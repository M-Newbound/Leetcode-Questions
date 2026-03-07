class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(t)
        left = 0
        best = (float('inf'), 0, 0)

        for right, c in enumerate(s):
            if need.get(c, 0) > 0:
                missing -= 1
            need[c] = need.get(c, 0) - 1

            while missing == 0:
                if right - left < best[0]:
                    best = (right - left, left, right)
                need[s[left]] = need.get(s[left], 0) + 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best[0] == float('inf') else s[best[1]:best[2] + 1]


# sliding window with a need counter, O(n) time

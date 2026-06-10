class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            nxt = node[char]
            if '#' in nxt:
                res.append(nxt['#'])
                del nxt['#']
            board[r][c] = '*'
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                    dfs(nr, nc, nxt)
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res


# might come back and clean this up later

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = [(r, c)]
            visited.add((r, c))
            while q:
                row, col = q.pop(0)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == '1' and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        return count


# there's probably a cleaner way to do this

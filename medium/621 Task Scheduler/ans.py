from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)
        time = 0
        q = []  # (available_time, count)
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append((time + n, cnt))
            if q and q[0][0] == time:
                heapq.heappush(heap, q.pop(0)[1])
        return time

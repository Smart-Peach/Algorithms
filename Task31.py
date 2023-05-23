from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def dfs():
            for vertex in range(len(edges)):
                visited[vertex] = 0

            m = -1
            for i in range(len(edges)):
                result = dfs_visit(i, 0, i, -1)
                m = max(m, result)
            return m

        def dfs_visit(edge, time, begin, res):
            if edge == -1:
                return res

            if not visited[edge]:
                visited[edge] = (1, begin)
                time_open[edge] = time
                time += 1
                res = dfs_visit(edges[edge], time, begin, res)
            else:
                if visited[edge][1] == begin:
                    res = max(res, time - time_open[edge])
            return res

        visited = {}
        time_open = {}

        return dfs()

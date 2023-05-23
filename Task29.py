from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def dfs(vertex, color):
            visited[vertex] = 1
            if not graph[vertex]:
                return True

            for vert in graph[vertex]:
                if not vert in colors:
                    colors[vert] = color
                else:
                    if colors[vert] != color:
                        return False

            color = not color
            for i in graph[vertex]:
                if not visited[i]:
                    res = dfs(i, color)
                    if not res:
                        return False

            return True

        if not graph:
            return False

        colors = {}
        visited = {}
        for i in range(len(graph)):
            visited[i] = 0

        flag = 1
        n = len(graph)
        for i in range(n):  # Ищем первую вершину, из которой хоть что-то выходит
            if graph[i]:
                flag = 0
                break

        if flag:  # Если все вершины без ребер, то возвращем тру
            return True

        for i in range(n):
            if i not in colors:
                res = dfs(i, False)
                if not res:
                    return False
        return True

class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        table = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        table[m - 1][n], table[m][n - 1] = 1, 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                table[i][j] = max(min(table[i + 1][j], table[i][j + 1]) - dungeon[i][j], 1)

        return table[0][0]
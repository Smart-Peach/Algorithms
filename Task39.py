class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_str, len_pat = len(s), len(p)
        table = [[False] * (len_pat + 1) for _ in range(len_str + 1)]
        table[0][0] = True
        for j in range(1, len_pat + 1):
            if p[j - 1] == '*':
                table[0][j] = table[0][j - 1]
        for i in range(1, len_str + 1):
            for j in range(1, len_pat + 1):
                if p[j - 1] == '*':
                    table[i][j] = table[i][j - 1] or table[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
        return table[len_str][len_pat]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m, n = len(s), len(p)
        len_str, len_pat = len(s), len(p)
        table = [[False] * (len_pat+1) for _ in range(len_str+1)]
        table[0][0] = True
        for j in range(1, len_pat+1):
            if p[j-1] == '*':
                table[0][j] = table[0][j-2]
            else:
                table[0][j] = j > 1 and p[j-2] == '*' and table[0][j-2]
        for i in range(1, len_str+1):
            for j in range(1, len_pat+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    table[i][j] = table[i-1][j-1]
                elif p[j-1] == '*':
                    table[i][j] = table[i][j-2] or (p[j-2] == s[i-1] or p[j-2] == '.') and table[i-1][j]
                else:
                    table[i][j] = False
        return table[len_str][len_pat]
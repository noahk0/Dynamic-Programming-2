def isMatch(self, s: str, p: str) -> bool:
    cache = {}

    def dfs(i, j):
        if (i, j) not in cache:
            if s[i:] == p[j:]:
                cache[(i, j)] = True
            elif len(p) <= j:
                cache[(i, j)] = False
            elif j + 1 < len(p) and p[j + 1] == '*':
                cache[(i, j)] = i < len(s) and (p[j] == '.' or p[j] == s[i]) and dfs(i + 1, j) or dfs(i, j + 2)
            else:
                cache[(i, j)] = i < len(s) and (p[j] == '.' or p[j] == s[i]) and dfs(i + 1, j + 1)

        return cache[(i, j)]

    return dfs(0, 0)

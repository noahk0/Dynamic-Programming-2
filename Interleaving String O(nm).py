def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2) or Counter(s3) != Counter(s1 + s2):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1)):
        if s3[i] != s1[i]:
            break
            
        dp[i + 1][0] = True

    for i in range(len(s2)):
        if s3[i] != s2[i]:
            break
            
        dp[0][i + 1] = True

    for i in range(len(s1)):
        for j in range(len(s2)):
            dp[i + 1][j + 1] = (dp[i][j + 1] and s3[i + j + 1] == s1[i]) or (dp[i + 1][j] and s3[i + j + 1] == s2[j])

    return dp[-1][-1]

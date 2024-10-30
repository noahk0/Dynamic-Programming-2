def minDistance(self, word1: str, word2: str) -> int:
    dp = list(range(len(word2) + 1))

    for i in range(len(word1)):
        pre, dp[0] = dp[0], i + 1

        for j in range(len(word2)):
            pre, dp[j + 1] = dp[j + 1], pre if word1[i] == word2[j] else min(pre, dp[j], dp[j + 1]) + 1

    return dp[-1]

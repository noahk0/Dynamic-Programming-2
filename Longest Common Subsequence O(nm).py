def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    s = set(text1)
    text2 = ''.join(c for c in text2 if c in s)
    s = set(text2)
    text1 = ''.join(c for c in text1 if c in s)

    if text1 == text2:
        return len(text1)

    for i in range(min(len(text1), len(text2))):
        if text1[i] != text2[i]:
            break

    s, text1, text2 = i, text1[i :], text2[i :]

    for i in range(min(len(text1), len(text2))):
        if text1[- i - 1] != text2[- i - 1]:
            break
        
    if i:
        s += i
        text1, text2 = text1[: - i], text2[: - i]

    dp = [0] * (len(text2) + 1)

    for i in range(len(text1)):
        new = [0]
        for j in range(len(text2)):
            new.append(dp[j] + 1 if text1[i] == text2[j] else max(dp[j + 1], new[j]))
                
        dp = new

    return s + dp[-1]

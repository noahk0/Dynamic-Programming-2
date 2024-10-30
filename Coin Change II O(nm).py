def change(self, amount: int, coins: List[int]) -> int:
    dp = [1] + [0] * amount

    for coin in sorted([coin for coin in coins if coin <= amount])[::-1]:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[-1]

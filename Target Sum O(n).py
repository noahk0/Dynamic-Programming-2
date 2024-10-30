def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1

    for num in nums[:-1]:
        new = defaultdict(int)

        for key in dp:
            new[key + num] += dp[key]
            new[key - num] += dp[key]

        dp = new

    return dp[target + nums[-1]] + dp[target - nums[-1]]

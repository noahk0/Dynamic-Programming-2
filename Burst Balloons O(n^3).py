def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + [n for n in nums if n] + [1]
    dp = [[0] * len(nums) for _ in range(len(nums))]
        
    for i in range(1, len(nums) - 1):
        for s in range(1, len(nums) - i):
            sub = nums[s - 1] * nums[s + i]
            dp[s][s + i] = max(sub * nums[piv] + dp[s][piv] + dp[piv + 1][s + i] for piv in range(s, s + i))

    return dp[1][-1]

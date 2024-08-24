from sys import *
from collections import *
from math import *

def tugOfWar(arr, n):
    total_sum = sum(arr)
    half_N = n // 2

    # DP table for storing possible sums with exactly i elements
    dp = [[False] * (total_sum + 1) for _ in range(half_N + 2)]
    dp[0][0] = True  # We can achieve a sum of 0 with 0 elements

    for num in arr:
        for i in range(half_N + 1, 0, -1):
            for j in range(total_sum, num - 1, -1):
                if dp[i - 1][j - num]:
                    dp[i][j] = True

    min_diff = float('inf')

    # For even n, we just check for half_N
    if n % 2 == 0:
        for i in range(total_sum // 2 + 1):
            if dp[half_N][i]:
                min_diff = min(min_diff, abs(total_sum - 2 * i))
    else:
        # For odd n, we check for both half_N and half_N + 1
        for i in range(total_sum // 2 + 1):
            if dp[half_N][i]:
                min_diff = min(min_diff, abs(total_sum - 2 * i))
            if dp[half_N + 1][i]:
                min_diff = min(min_diff, abs(total_sum - 2 * i))

    return min_diff




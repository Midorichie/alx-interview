def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): Values of coins in possession.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins needed, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Initialize dynamic programming table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update table for each amount from coin value to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, or -1 if impossible
    return dp[total] if dp[total] != float('inf') else -1


def change(amount, coins):
    """ Returns minimum number of coins required for given amount """

    # Base case
    if amount == 0:
        return 0

    # Return infinity if change is not possible
    if amount < 0 or coins == []:
        return float("inf")

    changeNext = change(amount, coins[1:])
    usedCoin = 1 + change((amount - coins[0]), coins)

    # Compares results to return best case
    return min(changeNext, usedCoin)

    

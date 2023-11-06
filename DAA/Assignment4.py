# Dynamic Programming
# Returns the maximum profit that can be stored by the bag
def knapSack(capacity, wt, profit, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]  # Matrix to store results
    print(capacity)
    # Fill the table in a bottom-up manner
    for i in range(n + 1):  # i = item
        for w in range(capacity + 1):  # w = capacity
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(profit[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][capacity]

# Main
profit = [50, 100, 150, 200]
wt = [8, 16, 32, 40]
capacity = 64
n = len(profit)
print(knapSack(capacity, wt, profit, n))
